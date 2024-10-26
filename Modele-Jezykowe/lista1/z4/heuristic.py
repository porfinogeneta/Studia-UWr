from typing import List
import random
import string

# nasza heurystyka będzie do oceny pytań czy z wyborem wariantów
class Heuristic:


    @staticmethod
    def remove_punctuation(input_text):
        # Translate table removes all punctuation characters
        translator = str.maketrans('', '', string.punctuation)
        cleaned_text = input_text.translate(translator)
        return cleaned_text
            
    def determine_answer(self, question: str) -> List[str]:

        question = Heuristic.remove_punctuation(question)

        words = question.split(" ")


        # pytania ze słowną odpowiedzią to pytania w stylu Czy … opc1 czy opc2?
        # je będziemy ewaluować sprawdzając czy odpowiedź jest w pierwszej albo drugiej połowie
        # powiemy, że odpowiedzieliśmy poprawnie, jeśli wybraliśmy dobrą połowę
        czy_idx = words.index("czy")
        first_half = " ".join(words[czy_idx-2:czy_idx])
        second_half = " ".join(words[czy_idx+1::])
        return random.choice([first_half, second_half])
        
    # q_a is a list of [question, [answer1, answer2]]
    def check_accuracy(self, q_a: List[List]) -> float:
        czy_answers =[p[1] for p in q_a]
        czy_questions = [p[0] for p in q_a]

        
        total = len(q_a)
        correct = 0

        for i in range(total):
            prediction = self.determine_answer(czy_questions[i])
            # prediction to string, sprawdzamy czy odpowiedź jest w tym stringu
            for ans in czy_answers[i]: 

                if ans in prediction:
                    # print(f"prediction {prediction} true answer: {ans}")
                    correct += 1
                    break

        return correct / total
                
