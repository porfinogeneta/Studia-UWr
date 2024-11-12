from typing import List
from sentence_prob import sentence_prob
import heapq
from tqdm import tqdm
# from quickselect import quick_select
text = """wprost|wyprosty|wyprostu|wyprost uwielbiała|wielbił|wielbiła|uwielbił|wielbiło|uwielbiał|uwielbiało|uwielbiały słuchać|osłuchać|słychać|usłuchać o|i|e|a|ó|ę|y|ą|u wartościach własnych|owłosionych macierzy|mocarz|macierzą|macierze|mocarza|mocarze|mocarzy|macierz"""

def tokenize_variants_text(text: str):
    types = text.split(" ")
    return [t.split("|") for t in types]
   

# our beam search hypothesis is that the sentence will have
# 6 words
class BeamSearch:

    BEAM_CONSTRAINT = 2

    def __init__(self, categories: List[str], k: int) -> None:
        self.categories = categories
        self.beams = k
        self.solutions = [[] for _ in range(k)]

  

    def traverse_tokens(self):
        # initialize ends as k most probable beginnings
        # initialization because there are some issues with same thing generated all the time
        token_probs = []
        for token in self.categories[0]:
            token_probs.append((sentence_prob(token), token))
        
        token_probs.sort(reverse=True)
        ends = [t for _, t in token_probs[:self.beams]]
        
        for category in tqdm(self.categories[1:]):
            token_probs = []
            for current_end in ends:
                for token in category:
                    s = f"{current_end} {token}".strip()
                    token_probs.append((sentence_prob(s), s))
            
            token_probs.sort(reverse=True)
            ends = [t for _, t in token_probs[:self.beams]]
            print(ends[0]) # most probable one
            print("Category end", 100 * "=")

        
           

if __name__ == "__main__":
    ctgs = tokenize_variants_text(text=text)
    search = BeamSearch(categories=ctgs, k=3)
    search.traverse_tokens()
