import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, LogitsProcessor
from tqdm import tqdm
import re
from typing import List
from collections import Counter
from trie import Trie
import torch.nn.functional as F
import logging


YELLOW = "\033[33m"
GREEN = "\033[32m"
RESET = "\033[0m"
logging.basicConfig(
    level=logging.DEBUG,
    format=f"{YELLOW}%(message)s{RESET}"
)

logger = logging.getLogger(__name__)


class OnlyCertainTokensAllowedLogitsProcessor(LogitsProcessor):
    def __init__(self, allowed_tokens, tokenizer = None) -> None:
        self.allowed_tokens = set(allowed_tokens)
        self.tokenizer = tokenizer

    def __call__(self, input_ids: torch.LongTensor, logits: torch.FloatTensor) -> torch.FloatTensor:
        
        modified_logits = logits.clone()

        # bierzemy wszystkie tokeny
        vocab_size = self.tokenizer.vocab_size
        all_tokens = [self.tokenizer.decode(i) for i in range(vocab_size)]

        print("allowed tokens", self.allowed_tokens)
        # tworzymy macierz, z -10000 dla tokenów dozwolonych
        p_mask = torch.tensor([
            0.0 if token in self.allowed_tokens else -10000.0 for token in all_tokens
        ], device=logits.device)

        # dodajemy maskę
        modified_logits[..., :vocab_size] += p_mask

        return modified_logits


class RiddlesSolver:

    model_name = "eryk-mazus/polka-1.1b"
    # model_name= "flax-community/papuGaPT2"

    device = "cpu"

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name,
                torch_dtype=torch.float32).to(device)
    




    def __init__(self, force_words) -> None:
        self.force_words = force_words


        # inicjalizując klasę, chcemy mieć już przygotowane drzewo po którym będziemy chodzić
        self.tokens_trie = Trie()

        for w in self.force_words:
            token_ids = self.tokenizer.encode(w, return_tensors="pt")
            # print(tokens_ids)
            tokens = self.tokenizer.convert_ids_to_tokens(token_ids[0])
            
            # pozbywamy się formatowania zdekodowanych tokenów
            clean_tokens = [token.replace('Ġ', '').replace('▁', '').replace("<s>", "") for token in tokens]
            clean_tokens = [token for token in clean_tokens if token and 
                        not token.startswith('[') and 
                        not token.endswith(']')]
            
            self.tokens_trie.insert(clean_tokens)

        self.tokens_trie.traverse_dfs(self.tokens_trie.root, "")

    
    def get_top_tokens(self, logits: torch.FloatTensor, k: int = 5) -> List[tuple]:
        last_token_logits = logits[0, -1, :]
        
        probabilities = F.softmax(last_token_logits, dim=0)
        
        top_probs, top_indices = torch.topk(probabilities, k)
        
        results = []
        for prob, idx in zip(top_probs.tolist(), top_indices.tolist()):
            token = self.tokenizer.decode(idx)
            results.append((token, prob))
        
        results.sort(key=lambda x: x[1], reverse=True)
        
        print("\nTop", k, "tokens and their probabilities:")
        for token, prob in results:
            print(f"Token: '{token}', Probability: {prob:.4f}")
            
        return results
    

    def generate(self, prompt: str) -> str:
        current = self.tokens_trie.root

        while not current.is_word_end:
            model_inputs = self.tokenizer.encode(prompt, return_tensors="pt")
            model_inputs = model_inputs.to(self.device)
            
            with torch.no_grad():

                outputs = self.model(model_inputs)
                logits = outputs.logits

                allowed_tokens = [token for token in current.children.keys()]
                if not allowed_tokens: break # czasami nie przechodzimy poprawnie po trie, czemu!?
                print("allowed tokens ", allowed_tokens)
                
                biased_processor = OnlyCertainTokensAllowedLogitsProcessor(allowed_tokens=allowed_tokens, tokenizer=self.tokenizer)
                biased_logits = biased_processor(input_ids=model_inputs, logits=logits)
                
                self.get_top_tokens(biased_logits)

                generated_ids = self.model.generate(
                    model_inputs,
                    max_new_tokens=1,
                    do_sample=True,
                    top_k=3,
                    top_p=0.95,
                    logits_processor=[biased_processor] 
                )
            
            res = self.tokenizer.decode(generated_ids[0], skip_special_tokens=True)
            generated_token = res[len(prompt):]
            # print(generated_token)
            current = current.children[generated_token.strip()] # przechodzimy po drzewie trie do odpowieniej gałęzi
            prompt = res
            logger.info(f"{GREEN}{res}{RESET}")
            
            if current.is_word_end:
                break

        
        return prompt



            