from typing import List
import time

array = [-45.02, -69.34, -23.58, -88.41, -12.76, -57.19, -35.64, -72.81, -91.53, -19.42, -66.78]


def partition(arr: List[float], left, right):
    pivot = arr[right]
    # elements ≤ pivot are left to this index
    smaller_pivot = left
    for i in range(left, right):
        if arr[i] >= pivot:
            arr[i], arr[smaller_pivot] = arr[smaller_pivot], arr[i]
            smaller_pivot += 1
    
    arr[smaller_pivot], arr[right] = arr[right], arr[smaller_pivot]
    
    return smaller_pivot

# print(partition(array, 0, len(array) - 1))
# print(array)
def quick_select(arr: List[float], k, left, right):
    if left == right:
        return arr[left]
    partition_idx = partition(arr, left, right)
    # search the left branch
    if partition_idx > k:
        return quick_select(arr, k, left, partition_idx - 1)
    # search the right branch
    elif partition_idx < k:
        return quick_select(arr, k, partition_idx + 1, right)
    else:
        return arr[k]

def measure_times(array: List[float], k: int, trials: int = 1000):
    sort_start = time.time()
    for _ in range(trials):
        sorted_result = sorted(array, reverse=True)[k]
    sort_end = time.time()
    
    quick_select_start = time.time()
    for _ in range(trials):
        quick_select_result = quick_select(array.copy(), k, 0, len(array) - 1)
    quick_select_end = time.time()

    sort_time = (sort_end - sort_start) / trials
    quick_select_time = (quick_select_end - quick_select_start) / trials

    print(f"Average time for sorting method: {sort_time:.6f} seconds")
    print(f"Average time for quick_select method: {quick_select_time:.6f} seconds")
    print(f"Result using sorted: {sorted_result}")
    print(f"Result using quick_select: {quick_select_result}")

k = 3
measure_times(array, k)