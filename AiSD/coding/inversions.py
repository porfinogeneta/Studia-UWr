
def mergesort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2


    L = mergesort(arr[:mid])
    R = mergesort(arr[mid:])

    i = j = k = 0

    # łączymy obie tablice, nadpisując tablicę z obecnego poziomu rekursji
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1

    return arr


def inversions(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    L, Linver = inversions(arr[:mid])
    R, Rinver = inversions(arr[mid:])

    i = j = k = inver = 0
    # łączymy obie tablice, nadpisując tablicę z obecnego poziomu rekursji
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
        elif L[i] > R[j]:
            arr[k] = R[j]
            # dodajemy inwersję, gdy element w lewej części jest większy niż w prawej
            # skoro ciągi są posortowane rosnąco to sprawdzamy za każdym razem
            # kolejny największy element, a zatem jeśli element z ciągu lewego jest największy
            # dla aktualnie największego prawego to musi też być największy dla pozostałych elementów,
            # sprawdzonych do tego momentu (stąd + j)
            inver += 1 + j
            j += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1

    return arr, Linver + Rinver + inver



if __name__ == "__main__":
    print(mergesort([2,8,5,3,9,4,1,7]))
    print(inversions([2,8,5,3,9,4,1,7]))