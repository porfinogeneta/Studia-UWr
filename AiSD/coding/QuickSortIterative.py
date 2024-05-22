import math

def partition(A, left, right):
    pivot = (left + right) // 2  # środkowy element to nasz pivot
    A[pivot], A[right] = A[right], A[pivot]  # wrzucamy pivot na koniec, żeby nie przeszkadzał
    pivot = right
    right -= 1
    while left < right:
        if A[left] < A[pivot]:
            left += 1
        # po prawej chcemy mniejsze równe elementy
        if A[right] >= A[pivot]:
            right -= 1
        # jak znaleźliśmy parę indeksów do zamiany, to zamieniamy
        if A[left] >= A[pivot] > A[right]:
            A[left], A[right] = A[right], A[left]
            left += 1
            right -= 1

    A[left], A[pivot] = A[pivot], A[left]

    return left


def quicksort(A):
    r = 0  # niezmiennik, tablica [0, r-1] posortowana
    while r < len(A):
        mx = r + 1  # największy element
        while mx < len(A) and A[mx] < A[r]:
            mx += 1
        if mx == r + 1:
            r += 1
        else:
            pivotIdx = partition(A, r + 1, mx - 1)  # dzielimy tablicę i podajemy indeks pivota
            A[pivotIdx], A[r] = A[r], A[pivotIdx]

    return A

if __name__ == "__main__":
    arr = [3,42,1,1,1,50,1, 2, 6,5,5,5, 4, 8,12, 4, 9,-1, 34]

    V = [54.3, 61.8, 72.4, 88.7, 118.6, 194.0]
    P = [61.2, 49.5, 37.6, 28.4, 19.2, 10.1]
    res = 0
    for i in range(6):
        # res += (X[i] - 7)*(Y[i] - 5)
        # res += (X[i] - 7)**2
        res+= (math.log(V[i]) - 4.49)**2
    ## 84
    # -0.25963655436228833

    print(res/6)
    # arr = [1, 1, 1, 1, 1, 1]
    # print(partition(arr, 0, len(arr) - 1))
    # print(quicksort(arr))
