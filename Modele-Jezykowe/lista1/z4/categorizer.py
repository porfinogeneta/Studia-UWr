import re
from typing import List
import csv

class Categorizer:

    def __init__(self) -> None:
        pass

    def _categorize(self, question: str) -> str:
        words = question.split(" ")

        czy_pattern = r"\bCzy\b"
        jak_pattern = r"\bJak ?(i|im|iej|iego|ą|ie)?\b"
        ile_pattern = r"\bIle\b"
        w_ktor_pattern = r"\bW ?który(m|ej|ch)?\b"
        kto_pattern = r"\bKto\b"

        if re.fullmatch(w_ktor_pattern, " ".join(words[:2])):
            return "w_ktorym+"
        elif re.fullmatch(czy_pattern, words[0]):
            if "czy" in words[1:]:
                return "czy_opt"
            else: return "czy"
        elif re.fullmatch(jak_pattern, words[0]):
            return "jak+"
        elif re.fullmatch(ile_pattern, words[0]):
            return "ile"
        elif re.fullmatch(kto_pattern, words[0]):
            return "kto"
        else:
            return "rest"

    def categorize_txt(self, filepath_questions, filepath_answers) -> dict:
        cat_types = ["czy", "czy_opt", "jak+", "ile", "w_ktorym+", "kto", "rest"]
        categories = {cat_type: [] for cat_type in cat_types}

        answers = self.read_answers_txt(filepath_answers)

        with open(filepath_questions, mode="r") as file:
            lines = file.readlines()

            for i in range(len(lines)):
                category = self._categorize(question=lines[i])
                categories[category].append([lines[i].strip(), answers[i]])
        
        return categories
    
    def read_answers_txt(self, filepath) -> List[str]:
        answers = []
        with open(filepath, "r") as file:
            for l in file:
                answers.append(l.strip().split("\t"))
        
        return answers




