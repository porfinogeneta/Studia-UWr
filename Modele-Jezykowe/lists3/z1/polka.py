import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from typing import List, Literal, Callable
from tqdm import tqdm
import string
import random
from prompts import get_prompt
import re
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class PolkaCalculator():
    
    def __init__(self) -> None:

        
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


    def generate(self, prompt: str) -> str:

        # response_inst_idx = len(prompt.split("[INST]")) - 1
        response_inst_idx = len(re.findall(r"\[INST\]", prompt)) - 1

        model_inputs = self.tokenizer([prompt], return_tensors="pt").to(self.device)
        with torch.no_grad():
            generated_ids = self.model.generate(
                **model_inputs,
                max_new_tokens=150,
                do_sample=True,
                penalty_alpha=0.6,
                top_k=10
            )

        res = self.tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
        # print("prompt part: ", res, "\n==========================", res[len(prompt):], '\n===========================')
        res_split = res.split("[INST]")
        
        # res_split[response_inst_idx:]
        text = " ".join(res_split[response_inst_idx:]) # generated text + prefix from prompt question
        cleared_prefix_txt = re.sub(r".*?\[/INST\]", "", text).strip() # get rid of prefix
        pattern = r'-?\d+(?:\.\d+)?' # pattern for number

        pattern = r'-?\d+(?:\.\d+)?'
        first_number_match = re.search(pattern, cleared_prefix_txt)
        first_number = first_number_match.group() if first_number_match else None

        # # Logging results
        # logger.debug("Decoded result (res): %s", res)
        # logger.debug("Cleared prefix text: %s", cleared_prefix_txt)
        # logger.info("First number found: %s", first_number)

        return first_number

        # matches = re.findall(pattern, res_split[response_inst_idx])
        # # jak nie ma matchy to dodaliśmy [INST] do odpowiedzi, przeszukujemy kolejny indeks [INST]
        # if not matches and response_inst_idx + 1 < len(matches):
        #     matches = re.findall(pattern, res_split[response_inst_idx + 1])

        # return matches[-1] if matches else None # ostatnie liczba z pierwszej wygenerowanej odpowiedzi
    
    def __count(self, a1: int, a2: int, op: str):
        if op == "+":
            return a1 + a2
        elif op == "-":
            return a1 - a2
        elif op == "*":
            return a1*a2
        elif op == "/":
            return a1//a2
    

    def determine_accuracy(self, prompt_type: str, complexity: str, rg: tuple, operation: str, total: int = 20) -> float:
        correct = 0
        
        start,end = rg
        for _ in tqdm(range(total)):
            n1 = random.randint(start,end)
            n2 = random.randint(start,end)

            prompt = get_prompt(prompt_type=prompt_type, complexity=complexity, n1=n1, n2=n2)

            # print(prompt)
            
            result = self.generate(prompt=prompt)
            try:
                int(result)
            except (ValueError, TypeError):
                raise ValueError(f"Not an intiger! -> {result}")

            true_res = self.__count(n1, n2, op=operation)
            print(f"{n1} {operation} {n2} = {result} | {true_res == int(result)}")
            if true_res == int(result):
                correct += 1
        
        accuracy = correct / total

        line = f"Accuracy: {accuracy}\nprompt_type: {prompt_type}\ncomplexity: {complexity}\ncorrect: {correct}\ntotal: {total}"
        with open(f"results_{prompt_type}_{complexity}.txt", 'w', encoding="utf-8") as file:
            print(line, file=file)
        
        return accuracy


