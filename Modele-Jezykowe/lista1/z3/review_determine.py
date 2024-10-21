import math
from typing import List
from sentence_probability import SentenceProabability
from tqdm import tqdm


class ReviewDetermine(SentenceProabability):
    def __init__(self) -> None:
        super().__init__()
        self.__scale = 0

    # true - positive, false - negative
    def determine_opinion(self, opinion: str, pos_neg: List[str]) -> bool:
        
        self.__scale = self.__normalize_probability(pos_neg)

        pos_rev, neg_rev = pos_neg
        
        def calc(whole_opn):
            return self.sentence_prob(whole_opn)

        log_prob_pos = calc(opinion + pos_rev)
        log_prob_neg = calc(opinion + neg_rev)


        # zmiana na liniowe PPB
        lin_prob_pos = math.exp(log_prob_pos)
        lin_prob_neg = math.exp(log_prob_neg)

        # print()
        # print(lin_prob_pos)
        # print(lin_prob_neg)
        # print(self.__scale)
        # print()

        scaled_lin_prob_neg = lin_prob_neg * self.__scale

        # print("positive: ", pos)
        # print("negative: ", neg)

        return lin_prob_pos > scaled_lin_prob_neg

    # zwraca liniową skalę
    def __normalize_probability(self, pos_neg: List[str]) -> float:

        # wyniki są w skali logarytmicznej
        probab_log_pos, probab_log_neg = [self.sentence_prob(s) for s in pos_neg]

        # zmieniamy na skalę liniową
        lin_prob_pos = math.exp(probab_log_pos)
        lin_prob_neg = math.exp(probab_log_neg)


        scale = lin_prob_pos / lin_prob_neg

        # print("positive probability: ", lin_prob_pos)
        # print("negative probability: ", lin_prob_neg)
        # print("negative: ", lin_prob_neg * scale)
        # print("scale factor:", scale)

        return scale
        

    def calculate_accuracy(self, filename: str, pos_neg: List[str], every_ith: int = 1) -> None:
        if every_ith <= 0: every_ith = 1
        content = ""
        with open(filename, "r") as f:
            content = [tuple(elem.split(" ", 1)) for elem in f.readlines()] 
        
        total = len(content)
        correct = 0


        for i in tqdm(range(0, total, every_ith)):
            feedback, opinion = content[i]
            r = self.determine_opinion(opinion, pos_neg)
            if r and feedback == "GOOD" or not r and feedback == "BAD":
                correct += 1
        

        with open("accuracy.txt", "a") as file:
            print(f"Dla parametrów: {pos_neg[0]} | {pos_neg[1]} \nCorrect: {correct} \n Total: {total // every_ith} \n % correct:  {correct / (total // every_ith)} \n", file=file)



