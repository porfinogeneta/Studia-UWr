import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from categorizer import Categorizer
from prompts import create_propmpt
from typing import List, Literal
from tqdm import tqdm
import string
import re


class PolkaQuizSolver(Categorizer):
    
    def __init__(self) -> None:
        super().__init__()

        self.model_name = "eryk-mazus/polka-1.1b"
        
        # self.device = (
        #     "mps" 
        #     if torch.backends.mps.is_available() 
        #     else "cpu"
        # )

        self.device = "cpu"
        
        print(f"Using device: {self.device}")
        
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForCausalLM.from_pretrained(
            self.model_name,
            torch_dtype=torch.float32
        ).to(self.device)
    
    def answer_question(self, question: str, prompt_type: Literal["zero", "one", "few"], questions: List[tuple], category: str) -> str:
       
        category = self._categorize(question=question)

        prompt = create_propmpt(question=question,
                                questions=questions, 
                                category=category,
                                prompt_type=prompt_type)

 
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
            model_ans = self.answer_question(question=q,
                                            prompt_type=prompt_type,
                                            questions=categories_dict[category],
                                            category=category)
            print(10* "=", "\nmodel: ", model_ans, "\n", 10 * "=", '\n', a_lst)
            # sprawdzamy czy jakikolwiek element z listy odpowiedzi jest w odpowiedzi modelu
            for a in map(str.lower, a_lst):
                if a in model_ans:
                    correct += 1
                    break
    
        return correct / total, correct, total
                
        
       
                
    def clean_text(self, text: str) -> str:
        text = re.sub(r'\s+', ' ', text)
        text = text.translate(str.maketrans('', '', string.punctuation))
        return text.strip().lower()


    def __generate(self, prompt: str) -> str:

        clean_prompt = self.clean_text(prompt)

        model_inputs = self.tokenizer([prompt], return_tensors="pt").to(self.device)
        with torch.no_grad():
            generated_ids = self.model.generate(
                **model_inputs,
                max_new_tokens=30,
                do_sample=True,
                penalty_alpha=0.6,
                top_k=10
            )

        
        prompt_len = len(clean_prompt)
        response = self.tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
        print(response)
        return self.clean_text(response)[prompt_len:]

