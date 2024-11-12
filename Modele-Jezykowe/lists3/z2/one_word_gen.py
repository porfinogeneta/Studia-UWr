

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from tqdm import tqdm
import re
from typing import List
from collections import Counter


class PrefixEnding:

    model_name = "eryk-mazus/polka-1.1b"

    device = "cpu"

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name,
                torch_dtype=torch.float32).to(device)


    def __init__(self, force_words: set) -> None:
        self.force_words = force_words


    def solve_riddle(riddle: str) -> str:
        """
            Bierzemy zagadkę, odpowiedź do niej. W bazie odpowiedzi szukamy kilku odpowiedzi
            o podobnej długości. Generujemy odpowiedź.
        """

        prompt = """"""


    def __clean_text(self, text: str) -> str:
        return ' '.join(text.split()).lower()
    

    def generate(self, prompt: str) -> str:
        input_ids = self.tokenizer(prompt, return_tensors="pt").input_ids

        force_words_ids = self.tokenizer(self.force_words, add_special_tokens=False).input_ids
        # print(model_inputs)

        """
            https://huggingface.co/blog/how-to-generate
            https://huggingface.co/blog/constrained-beam-search
            num_beams - ile mamy ścieżek znajdowania prawdopodobieństw
            early_stopping - generacja się kończy, kiedy wszystkie beamy dojdą do końca
            no_repeat_ngram_size - dodanie kary za powtarzanie jednego ze słów
            num_return_sequences - ile najlepszych beamów mamy zwrócić ≤ num_beams
            do_sample - wybieraj losowo kolejny token, na podstawie rozkładu ppb warunkowego
            temperature - zwiększamy ppb bardziej ppb i zmniejszamy ppb mniej ppb
            top_k - wybieramy k najlepszych i ppb jest redystrybuowane wśród nich
            top_p (nucleus) - bierze ppb przekraczające jakiś treshhold

        """

        outputs = self.model.generate(
            input_ids,
            force_words_ids=force_words_ids,
            num_beams=7,
            num_return_sequences=7,
            remove_invalid_values=True,
        )

        force_set = set(self.force_words)
        results = []

        for i, o in enumerate(outputs):
            # usuwamy nadmiarowe spacje, zmniejszamy wielkość liter
            result = self.__clean_text(self.tokenizer.decode(o, skip_special_tokens=True))
            print(result)
            # przejdziemy po zwróconym stringu i wzrócimy pierwszy wyraz z odpowiedzi będący wyrazem z force words
            result_split = result.split(" ")
            for w in result_split:
                if w in force_set:
                    print(f"{i}. Output:\n")
                    print(w)
                    print(100*"-")
                    results.append(w)
                    break
        
        return Counter(results).most_common(1)[0]
    


            

            