import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from categorizer import Categorizer
from prompts import get_prompt
from typing import List, Literal
from tqdm import tqdm
import string


class PolkaQuizSolver(Categorizer):
    
    def __init__(self) -> None:
        super().__init__()

        self.model_name = "eryk-mazus/polka-1.1b"
        
        self.device = (
            "mps" 
            if torch.backends.mps.is_available() 
            else "cpu"
        )
        
        print(f"Using device: {self.device}")
        
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForCausalLM.from_pretrained(
            self.model_name,
            torch_dtype=torch.float32
        ).to(self.device)
    
    def answer_question(self, question: str, prompt_type: Literal["zero", "one", "few"]) -> str:
       
        category = self._categorize(question=question)

        prompt = get_prompt(
            question=question,
            category=category,
            prompt_type=prompt_type
        )
        
        
        return self.__generate(prompt=prompt)
    

    # q_ato lista złożona z [question, [answer1, answer2]]
    def check_accuracy(self, 
                       categories_dict: dict,
                        prompt_type: Literal["zero", "one", "few"],
                        category: Literal["czy", "czy_opt", "jak+", "ile", "w_ktorym+", "kto", "rest"],
                        amount_from_category: int = 5
                        ) -> float:

        total = len(categories_dict[category][:amount_from_category])
        correct = 0
        # q - pytanie, a_lst - lista odpowiedzi
        for q, a_lst in tqdm(categories_dict[category][:amount_from_category]):
            model_ans = self.remove_punctuation(self.answer_question(question=q, prompt_type=prompt_type).lower())
            print("model: ", model_ans, "answers: ", a_lst)
            for a in map(str.lower, a_lst):
                print(a)
                if a in model_ans:
                    correct += 1
                    print("is in answer")
                    break
    
        return correct / total, correct, total
                
        
       
                
    def remove_punctuation(self, input_text):
        # Translate table removes all punctuation characters
        translator = str.maketrans('', '', string.punctuation)
        cleaned_text = input_text.translate(translator)
        return cleaned_text


    def __generate(self, prompt: str) -> str:


        model_inputs = self.tokenizer([prompt], return_tensors="pt").to(self.device)
        with torch.no_grad():
            generated_ids = self.model.generate(
                **model_inputs,
                max_new_tokens=150,
                do_sample=True,
                penalty_alpha=0.6,
                top_k=20
            )

        return self.tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0][-30:] # bierzemy 30 ostatnich znaków

