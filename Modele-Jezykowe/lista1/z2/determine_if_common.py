from tqdm import tqdm
from typing import List
from txt_prob import sentence_prob

class DetermineIfCommon:

    def __init__(self) -> None:
        pass

    def parse_sentence(self, sentence: str) -> List[str]:
        words = sentence.split()
        words[0] = words[0].lower()
        words[-1] = words[-1][:-1]

        return words

    def generate_all_pairs(self, lst: List[str]) -> List[tuple]:
        pairs = []
        for i in range(len(lst)):
            for j in range(i+1, len(lst)):
                pairs.append((lst[i],lst[j]))
                pairs.append((lst[j],lst[i]))

        return pairs
    
    def find_best_pairs(self, words: List[str], lst_pairs: List[tuple]):
        """
            given a list of pairs, returnes a pairs set, that yields
            the highest probability in the sentece overall,
            greedy approach
        """

        # dict: pair: prob (log)
        dict_prob = {pair: None for pair in lst_pairs}
        for p1,p2 in dict_prob.keys():
            prob_combined = sentence_prob(f"{p1} {p2}")
            prob_separated = sentence_prob(p1) + sentence_prob(p2)
            delta = prob_separated - prob_combined
            dict_prob[(p1, p2)] = delta
            # if delta < 4.5:
            #     print(f"Combined: {prob_combined};\nSeparated: {prob_separated};\nImprovement: {delta}")
            #     print(f"Result for: {p1} {p2}")
        # dict_prob = {pair: sentence_prob(f"{pair[0]} {pair[1]}") for pair in lst_pairs}
        # sorted dict according to probability
        dict_prob = dict(sorted(dict_prob.items(), key= lambda item: item[1], reverse=False))
        # print(dict_prob)
        used = set()
        not_used = set(words)

        # according to greedy approach
        best_words_blend = []

        for p1, p2 in dict_prob.keys():
            if p1 not in used and p2 not in used:
                if dict_prob[(p1, p2)] < 5.5:
                    best_words_blend.append(f"{p1} {p2}")
                    used.add(p1), used.add(p2)
                    not_used.remove(p1), not_used.remove(p2)
        
        
        while not_used:
            best_words_blend.append(not_used.pop())
        # not even amount of words, one will be alone :(
        # if len(not_used) == 1:
        #     best_words_blend.append(not_used.pop())

        return best_words_blend




    def generate_sentences_permutations(self, words: List[str]) -> str:
        """
            for a given list of words, generates all permutations
            of a sentence, returnes list of possiblr permutations
        """

        def permute(words):
            if words == []:
                return [[]]
            
            perms = permute(words[1:])
            res = []

            for p in perms:
                for i in range(0, len(p) + 1):
                    l_cpy = list(p)
                    l_cpy.insert(i, words[0])
                    res.append(l_cpy)
            
            return res

        sentences_words_lst = permute(words)

        # prepare sentences, capitalize first word, add . at the end
        sntsc = [" ".join([w.capitalize() if i == 0 else (w + "." if i == len(sen) - 1 else w) for i, w in enumerate(sen)]) for sen in sentences_words_lst]
        
        return sntsc
    
    def find_the_most_natural_sentences(self, sentence: str, filename: str) -> None:
    
        words = self.parse_sentence(sentence=sentence)

        if len(words) < 6:
            # short enough sentences
            all_sntc_perm = self.generate_sentences_permutations(words)
            print(all_sntc_perm)
        else:
            # long sentences
            pairs = self.generate_all_pairs(words)
            blended_words = self.find_best_pairs(words=words, lst_pairs=pairs)
            print(blended_words)
            # generate all permutations of blended words
            all_sntc_perm = self.generate_sentences_permutations(blended_words)
        
        # calculate probability of each sentence, and sort it
        # res = {snt: sentence_prob(snt) for snt in tqdm(all_sntc_perm)}
        res = {all_sntc_perm[i]: sentence_prob(all_sntc_perm[i]) for i in range(100)}
        res = dict(sorted(res.items(), key= lambda item: item[1], reverse=True))

        with open(filename, "w") as f:
            for key, val in res.items():
                f.write(f"{key} {val}\n")
                
            f.close()


        
        