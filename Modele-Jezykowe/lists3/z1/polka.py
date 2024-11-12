import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from typing import List, Literal, Callable
from tqdm import tqdm
import string
import random
import re
import logging
import pandas as pd
import matplotlib.pyplot as plt

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
        """
            To make generate work we need to have covered that the prompt will end with instruction.
            Generate finds the end of last prompt instruction and returnes the first number after the end
            (we assume that's the generated answer). Works for all prompts ending in instruction.
        """

        # nie odejmujemy 1 bo po split system prompt to 0 indeks
        response_inst_idx = len(re.findall(r"\[INST\]", prompt))

        prompt_len = len(self.__clean_text(prompt))

        model_inputs = self.tokenizer([prompt], return_tensors="pt").to(self.device)
        with torch.no_grad():
            generated_ids = self.model.generate(
                **model_inputs,
                max_new_tokens=10,
                do_sample=True,
                penalty_alpha=0.6,
                top_k=10
            )

        res = self.tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
        clear_res = self.__clean_text(res)

        pattern = r'-?\b\d+\b' # pattern for number

        first_number_match = re.search(pattern,  clear_res[prompt_len:])
        first_number = first_number_match.group() if first_number_match else None

        # # Logging results
        logger.debug("Decoded result (res): %s", res)
        logger.debug("Cleared prefix text: %s", clear_res[prompt_len:])
        logger.info("First number found: %s", first_number)

        return first_number


    def __count(self, a1: int, a2: int, op: str):
        if op == "+":
            return a1 + a2
        elif op == "-":
            return a1 - a2
        elif op == "*":
            return a1*a2
        elif op == "/":
            return a1//a2
        


    def __clean_text(self, text: str) -> str:
        text = text.replace('\n', ' ')
        
        tags_to_remove = ["[INST]", "[/INST]", "<<SYS>>", "<</SYS>>", "<s>"]
        for tag in tags_to_remove:
            text = text.replace(tag, '')

        return text.lower().strip()
    

    def determine_accuracy( self, 
                            operation: str,
                            operation_type:str,
                            complexity: str,
                            rg: tuple,
                            prompt_generator: Callable[[str, tuple, int], List[int]],
                            total: int = 20) -> float:
        """
            operation - operacja +/-/*//
            operation_type - addition/…
            rg - zakres liczb w działaniach
            total - na ilu przykładach ocenimy ppb
        """
        
        correct = 0
        for _ in tqdm(range(total)):

            PROMPT, arg1, arg2 = prompt_generator(operation, rg, 5)

            result = self.generate(prompt=PROMPT)
            
            try:
                int(result)
            except (ValueError, TypeError):
                # raise ValueError(f"Not an intiger! -> {result}")
                result = 0
                        
            true_res = self.__count(arg1, arg2, op=operation)
            
            print(f"{arg1} {operation} {arg2} = {result} | {true_res == int(result)}")
            
            if true_res == int(result):
                correct += 1
        
        accuracy = correct / total

        line = f"Accuracy: {accuracy}\noperation: {operation}\ncomplexity: {complexity}\ncorrect: {correct}\ntotal: {total}"
        with open(f"results/{operation_type}/{complexity}.txt", 'w', encoding="utf-8") as file:
            print(line, file=file)
        
        return accuracy
    
    
    def extract_and_plot_combined(self, files_dict):
        """
        Creates a single figure with multiple bar plots side by side.
        
        Parameters:
        files_dict (dict): Dictionary with keys as plot titles and values as lists of file paths
        """
        plt.figure(figsize=(20, 6))
        
        n_plots = len(files_dict)
        
        for idx, (title, file_paths) in enumerate(files_dict.items(), 1):
            data_list = []
            for file_path in file_paths:
                data = {}
                with open(file_path, 'r') as file:
                    for line in file:
                        key, value = line.strip().split(': ')
                        data[key] = float(value) if key in ['Accuracy', 'correct', 'total'] else value
                data_list.append(data)
            
            operations = [d['operation'] for d in data_list]
            accuracies = [d['Accuracy'] for d in data_list]
            
            plt.subplot(1, n_plots, idx)
            bars = plt.bar(operations, accuracies)
            
            plt.title(f"[{data['total']}] {title}", fontsize=12, pad=20)
            plt.xlabel('Operation', fontsize=10)
            plt.ylabel('Accuracy' if idx == 1 else '', fontsize=10)
            plt.ylim(0, 1.0)
            
            for bar in bars:
                height = bar.get_height()
                plt.text(bar.get_x() + bar.get_width()/2., height,
                        f'{height:.2%}',
                        ha='center', va='bottom',
                        fontsize=9)
            
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            
            plt.xticks(rotation=45)
        
        plt.tight_layout()
        plt.show()