# def main():
#     G = {1: [2, 3], 2: [4, 5], 3: [6], 4: [], 5: [], 6: []}
#     visited = [False] * len(G.keys())
#
#     q = 0
#
#     def dfs(visited, v, G):
#         # print(v)
#         q += 1
#         visited[v - 1] = True
#         for w in G[v]:
#             if not visited[w - 1]:
#                 dfs(visited, w, G, q)
#
#     dfs(visited, 0, G)
#     return q
#
#
# print(main())

def merge(X, Y):
    x = 0
    y = 0
    res = []
    while x < len(X) and y < len(Y):
        if X[x] <= Y[y]:
            res.append(X[x])
            x += 1
        elif X[x] > Y[y]:
            res.append(Y[y])
            y += 1

    while x < len(X):
        res.append(X[x])
        x += 1

    while y < len(Y):
        res.append(Y[y])
        y += 1
    return res

def merge_sort(T):
    if len(T) == 1:
        return T
    m1 = merge_sort(T[:len(T)//2])
    m2 = merge_sort(T[len(T)//2:])
    return merge(m1, m2)

# print(merge_sort([3,1,6,8,2,1,10,96, 42]))


# print(merge([1,3,5,7], [2,4,6,8,10,14]))
def partition(T, low, high):
    pivotIdx = (low + high) // 2
    T[high], T[pivotIdx] = T[pivotIdx],T[high]
    pivot = T[high]
    l = low
    r = high - 1
    while l <= r:
        # po lewej szukamy elementu większego od pivota, po prawej mniejszego
        if T[l] <= pivot:
            l += 1
        elif T[r] >= pivot:
            r -= 1
        else:
            T[l], T[r] = T[r], T[l]
            l += 1
            r -= 1

    T[l], T[high] = T[high], T[l]
    return l

def quicksort(T, low, high):
    if low >= high: return
    partition_point = partition(T, low, high)
    quicksort(T, low, partition_point)
    quicksort(T, partition_point + 1, high)


T = [3,5,1,23,8,1,16, 42, 18]
# K = [1,6,5,3]
# partition(K, 0, len(K) - 1)
# print(K)
quicksort(T, 0, len(T) - 1)
print(T)


