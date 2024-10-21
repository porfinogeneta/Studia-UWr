from itertools import permutations
from typing import List

# def generate_pair_combinations(nums):
#     res = []
#     perms = list(permutations(nums))
    
#     for perm1 in perms:
#         for perm2 in perms:
#             pairs = list(zip(perm1, perm2))  # This will zip elements from perm1 with perm2
#             res.append(pairs)
    
#     return res


# for e in generate_pair_combinations([1,2,3,4]):
#     print(e)

def generate_pair_combinations(nums):

    def gen_pairs(lst):
        if len(lst) < 2:
            return [lst]
        
        # nieparzyste listy
        if len(lst) % 2 == 1:
            result = []
            for i in range(len(lst)):
                pairs = gen_pairs(lst[:i] + lst[i+1:])
                for p in pairs:
                    result.append([[lst[i], lst[i]], p])
            return result
        else:
            # parzyste listy
            elem = lst[0]
            result = []
            for i in range(1, len(lst)):
                pairs = gen_pairs(lst[1:i] + lst[i+1:])
                for p in pairs:
                    result.append([[elem, lst[i]], p])

            return result
    result = gen_pairs(nums)
    return [[[pairs[i], pairs[i+1]] for i in range(0, len(pairs) - 1, 2)] for pairs in result]


def generate_all_pairs(lst: List[int]):
    pairs = []
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            pairs.append((lst[i],lst[j]))
            pairs.append((lst[j],lst[i]))

    return pairs

    
if __name__ == "__main__":
    # res = generate_pair_combinations([1,2,3,4,5,6,7,8,9,10,11])
    # print(len(res))

    # for x in res:
    #     print(x)
    generate_all_pairs([1,2,3,4])