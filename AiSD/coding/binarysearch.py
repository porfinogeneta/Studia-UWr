def binarysearch(array, target):
    l = 0
    r = len(array) - 1
    while l <= r:
        mid = (l + r) // 2
        if array[mid] == target:
            if array[mid - 1] == target:
                r = mid - 1
            else:
                return mid
        elif array[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    return -1


print(binarysearch([1,1,2,2,3,4,5,5,6], 2))


