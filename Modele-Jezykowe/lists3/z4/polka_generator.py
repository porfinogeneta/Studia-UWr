import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, LogitsProcessor
from typing import List, Literal, Callable
import logging
import torch.nn.functional as F
from tqdm import tqdm
import re

YELLOW = "\033[33m"
GREEN = "\033[32m"
RESET = "\033[0m"
logging.basicConfig(
    level=logging.DEBUG,
    format=f"{YELLOW}%(message)s{RESET}"
)

logger = logging.getLogger(__name__)




class BiasLogitsProcessor(LogitsProcessor):
    def __init__(self, letter: str, boost_factor: float = 2.0, tokenizer = None) -> None:
        self.letter = letter
        self.boost_factor = boost_factor
        self.tokenizer = tokenizer

    def __call__(self, input_ids: torch.LongTensor, logits: torch.FloatTensor) -> torch.FloatTensor:
        
        modified_logits = logits.clone()


        # bierzemy wszystkie tokeny
        vocab_size = self.tokenizer.vocab_size
        all_tokens = [self.tokenizer.decode(i) for i in range(vocab_size)]

       
        # tworzymy macierz, z 1 dla tokenów zaczynających się od letter albo Letter,
        # potem boost dodamy tylko do tych tokenów
        p_mask = torch.tensor([
            1.0 if token.startswith(self.letter.lower()) or token.startswith(self.letter.capitalize()) else 0 for token in all_tokens
        ], device=logits.device)

        boost = torch.log(torch.tensor(self.boost_factor))

        # dodajemy boost, ale tylko do tokenów zaczynających się od 'letter'
        modified_logits[..., :vocab_size] += boost*p_mask

        return modified_logits

class PolkaGenerator():
    
    def __init__(self) -> None:

        
        # self.model_name = "flax-community/papuGaPT2"
        self.model_name = "eryk-mazus/polka-1.1b"
        
        self.device = "cpu"
        
        print(f"Using device: {self.device}")
        
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForCausalLM.from_pretrained(
            self.model_name,
            torch_dtype=torch.float32
        ).to(self.device)


    def show_tokenization(self, text: str) -> None:
        """Display detailed tokenization information for the input text."""

        tokens = self.tokenizer.encode(text, return_tensors="pt")
        tokenized_text = self.tokenizer.convert_ids_to_tokens(tokens[0])

        # print("\n=== Tokenization Details ===")
        # print("Original text:", text)
        # print("\nTokens breakdown:")
        # for i, token in enumerate(tokenized_text):
        #     print(f"Token {i}: {token}")
                
        return tokens
    
    def get_top_tokens(self, logits: torch.Tensor, k: int = 10) -> None:
        probs = F.softmax(logits, dim=-1)
        top_probs, top_indices = torch.topk(probs, k)
        
        top_k_tokens = []
        # print("\n=== Top Next Token Probabilities ===")
        for prob, idx in zip(top_probs[0], top_indices[0]):
            token = self.tokenizer.decode([idx])
            probability = prob.item() * 100
            top_k_tokens.append(token)
            print(f"Token: '{token}' - Probability: {probability:.2f}%")

        return top_k_tokens

    def generate(self, prompt: str, letter: str) -> str:
        """
            Generate one token at a time.
        """

        model_inputs = self.show_tokenization(prompt)
        model_inputs = model_inputs.to(self.device)

        # top-p
        # samplujemy tylko z ppb, których suma wynosi podaną wartość
        # top-k
        # samplujemy tylko spośród k najbardziej ppb tokenów

        
        with torch.no_grad():

            outputs = self.model(model_inputs)
            logits = outputs.logits # logit'y to wyjścia z modelu

            # debug
            # self.get_top_tokens(logits[:, -1, :], k=20)

            # tylko jak TOP_P tokenów z TOP_K tokenów to tokeny rozpoczynający się
            # wielką literą albo _, wtedy dodajemy bias na literę
            # przy czym muszą to być tokeny 'literowe' czyli wykluczone są ,-! itp
            # top_k_tokens = self.get_top_tokens(logits[:, -1, :], k=TOP_K)

            # next_words_amount = 0
            # for tk in top_k_tokens:
            #     if self.is_new_word_beginning(tk):
            #         next_words_amount += 1
            
            # print(100*"=", "top-k", top_k_tokens)
            # # jak jest spore ppb że to początek słowa, wtedy dajemy bias
            # if next_words_amount / TOP_K > 0.5:
            biased_processor = BiasLogitsProcessor(letter=letter, boost_factor=20.0, tokenizer=self.tokenizer)
            biased_logits = biased_processor(input_ids=model_inputs, logits=logits)

            # print("\nBiased logits")
            # biased_tokens = self.get_top_tokens(biased_logits[:, -1, :], k=TOP_K)
            # for t in biased_tokens:
            #     print(t)
            

            generated_ids = self.model.generate(
                model_inputs,
                max_new_tokens=1,
                do_sample=True,
                top_k=10,
                top_p=0.90,
                logits_processor=[biased_processor] 
            )
        
        res = self.tokenizer.decode(generated_ids[0], skip_special_tokens=True)
        return res


    def end_prefix(self, prefix: str):
        letter = prefix[0]
        for _ in range(5):
            prefix = self.generate(prompt=prefix, letter=letter)
            if prefix.endswith(('.', ';', '?', '!')):
                break
        
        # logger.debug("\nFinal generated text: %s", prefix) 
        # zakańczamy prefix . jak nie doszliśmy do . w iteracji
        if not prefix.endswith(('.', ';', '?', '!')):
            last_space_idx = prefix.rfind(" ")
            if last_space_idx != -1:
                prefix = prefix[:last_space_idx] + "."
            else:
                prefix += "."


        return prefix
    
    def variants_generation(self, quantity: int, prefix: str):
        variants = []
        for _ in tqdm(range(quantity)):
            s = self.end_prefix(prefix=prefix)
            # print(s)
            # print(10 * "=")
            variants.append(s)

        return variants
    
    def find_best_variant(self, variants_quantity: int, prefix) -> str:
        """
            Finds the best sentence, the criteria is that each word in a sentence is began
            with specyfic letter and the sentence has the most of those letters.
        """
        sentences = self.variants_generation(quantity=variants_quantity, prefix=prefix)
        # sentences = ['Warto wypróbować więc w wolnej.','Warto wypróbować więc własną wiedzę!', 'Warto wypróbować więc wtedy w.', 'Warto wypróbować więc w wersji.', 'Warto wypróbować więc wyroby.']
        print(sentences)
        best = ""
        max_len = 0
        for s in sentences:
            s = s.replace("\\n", " ")
            # words = re.findall(r'\b\w+\b', s)
            # words = [w for w in words if w.isalpha()]
            
            all_start_with_given_letter = all(word.lower().startswith(prefix[0].lower()) for word in words)

            # czy spełniony jest warunek
            if all_start_with_given_letter:
                # wybieramy dłuższy tekst
                if len(s) > max_len:
                    best = s
                    max_len = len(s)
                
        logger.info(f"{GREEN}{best}{RESET}")
        return best