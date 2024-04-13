
def knapsack(coins, F):
    # lista problemów do rozwiązania, na pierwszej pozycji trzymamy nominał
    # na drugiej pozycji trzymamy monetę która wygenerowała nam najlepszą odpowiedź
    problems = [[float("-inf"), None] for _ in range(F + 1)]
    problems[0][0] = 0
    problems[0][1] = 0
    for p in range(1, len(problems)):
        for c in coins:
            # problem został rozwiązany
            if p - c[1] >= 0 and problems[p - c[1]][0] != float("-inf"):
                # porównujemy dany nominał i problem korzystnie rozwiązany dla niego
                # z wartością która już była wcześniej w tablicy
                if problems[p - c[1]][0] + c[0] > problems[p][0]:
                    problems[p][0] = problems[p - c[1]][0] + c[0]
                    problems[p][1] = coins.index(c)


    current = F
    # print(problems[current][1])
    res = [0 for _ in range(len(coins))] # lista w której będziemy trzymać liczbę konkretnej monety
    while current != 0:
        idx = problems[current][1]
        res[idx] += 1
        current -= coins[idx][1]
    print(res)


    return problems



if __name__ == "__main__":
    F = 10
    coins = [(1,2), (2,3), (2,5), (40,9)]
    print(knapsack(coins, F))