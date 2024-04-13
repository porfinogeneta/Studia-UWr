

# def partition(arr, start, end):
#     pivot = arr[start]
#     low = start + 1
#     high = end
#
#     while True:
#         while low <= high and arr[low] <= pivot:
#             low += 1
#         while low <= high and arr[high] >= pivot:
#             high -= 1
#
#         if low <= high:
#             arr[low], arr[high] = arr[high], arr[low]
#
#         else:
#             break
#     # przesuwamy pivota
#     arr[start], arr[high] = arr[high], arr[start]
#     return high
# def quicksort(arr, l, r):
#     if l >= r:
#         return
#     pi = partition(arr, l, r)
#     quicksort(arr, l, pi - 1)
#     quicksort(arr, pi + 1, r)

def allSubsequences(stillConsider, created, remaining):
    if remaining == 0:
        return created
    if remaining < 0:
        return
    if remaining != 0 and stillConsider == []:
        return

    # mamy dwie gałęzie, jedna bierze pierwszy element, druga nie
    res1 = allSubsequences(stillConsider[1:], created + [stillConsider[0]], remaining - stillConsider[0])
    res2 = allSubsequences(stillConsider[1:], created, remaining)

    if res1 != [] and res2 != []:
        return res1 + res2
    elif res1 == []:
        return res2
    else:
        return res1



if __name__ == "__main__":
    arr = [1,4,10, 2, 8]
    arr1 = [1,2,3]
    # partition(arr, 0, len(arr) - 1)
    # quicksort(arr, 0, len(arr) - 1)
    # print(arr)
    print(allSubsequences(arr1, [], 3))