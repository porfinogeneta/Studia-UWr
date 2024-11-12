from riddles_solver import RiddlesSolver
from trie import Trie
from riddles.riddles import riddles, answers
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from typing import List
import random

words = [
    "kot",         # 3 litery
    "las",         # 3 litery
    "zamek",       # 5 liter
    "okno",        # 4 litery
    "deszcz",      # 6 liter
    "szybko",
    "szybka",
    "szybciej",
    "słońce",      # 6 liter
    "czekolada",   # 9 liter
    "komputer",    # 8 liter
    "pociąg",      # 6 liter
    "książka",     # 7 liter
    "muzyka",      # 6 liter
    "telefon",      # 7 liter
    "prestidigitator"
]


def sample_n_answers(answers: List[str], amount: int):
    indices = random.sample(range(len(answers)), amount)
    return [answers[i] for i in indices]

if __name__ == "__main__":


    # force_words = sample_n_answers(answers=answers, amount=9)
    # force_words.append("lilia")
    # force_words.append("kino")
    # solver = RiddlesSolver(force_words=force_words)
    # prompt = f"wodna roślina pływająca, znana z pięknych, białych lub różowych kwiatów, to inaczej -"
    
    # finished_riddle = solver.generate(prompt=prompt)

    with open("pres_res.txt", 'w') as file:
        correct = 0
        total = min(10, len(riddles))
        for i,riddle in enumerate(riddles[:total]):
            # set of words, that we will choose answers from
            force_words = sample_n_answers(answers=answers, amount=10)
            force_words.append(answers[i])
            solver = RiddlesSolver(force_words=force_words)
            prompt = f"{riddle}, to inaczej -"
            
            finished_riddle = solver.generate(prompt=prompt)
            
            print("RIDDLE: ", prompt, file=file)
            
            guess = finished_riddle[len(prompt):].strip()
            
            print("GUESS: ", guess, file=file)
            print("SOLUTION: ", answers[i], file=file)
            
            if guess == answers[i]:
                correct += 1
        
        print("ACCURACY: ", correct / total, file=file)
    