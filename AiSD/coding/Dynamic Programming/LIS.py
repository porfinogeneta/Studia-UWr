
def LIS(arr):
    dp = [1 for _ in range(len(arr))]
    for i in range(1, len(arr)):
        j = 0 # wskaźnik idący do aktulnego indexu
        while j < i:
            if arr[j] < arr[i]:
                # czy można uzyskać lepszy wynik
                dp[i] = max(dp[j] + 1, dp[i])
            j += 1 # przesuwamy wskaźnik

    return max(dp)


def amountOfLIS(nums):
    if not nums:
        return 0

    # lista długości
    lgh = [1 for _ in range(len(nums))]
    # lista liczników, każdej z długości
    cnt = [1 for _ in range(len(nums))]

    # wartości, które są maksimami dotychczas znalezionych sekwencji
    lenLIS, count = 1, 1

    for i in range(1, len(nums)):
        for j in range(i):
            # porównujemy wszystkie liczby do i-tej
            if nums[i] > nums[j]:
                # jak możemy uzyskać większą długość
                if lgh[i] < lgh[j] + 1:
                    lgh[i] = lgh[j] + 1 # podmieniamy długości
                    cnt[i] = cnt[j] # counter przepisujemy z bardziej korzystnej wersji
                elif lgh[i] == lgh[j] + 1:
                    cnt[i] += cnt[j] # jak długości są takie same dostajemy dodatkowe ciągi

        # jak otrzymamy większą długość, update zmiennych globalnych
        if lgh[i] > lenLIS:
            lenLIS, count = lgh[i], cnt[i]
        # jak długości są te same to zwiększamy licznik, bo po prostu mamy kolejne pasujące sekwencje
        elif lgh[i] == lenLIS:
            count += cnt[i]

    return count



if __name__ == "__main__":
    # print(LIS([-1,2,4,3]))
    print(amountOfLIS([1,3,5,4,7]))
    print(amountOfLIS([2,2,2,2,2]))
