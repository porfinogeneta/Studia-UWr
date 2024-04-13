# zmiana elementu, i index do zmiany, u, nowa wartość
# implementacja dla kopców malejących w dół
def change_elem(K, i, u):
    x = K[i]
    K[i] = u
    # nowy element jest większy od starego, zaburzenie może iść w górę, wpp w dół
    if x < u:
        move_up(K, i)
    else:
        move_down(K, i)

def move_up(K, i):
    k = i
    j = -1
    while k != j:
        j = k
        # odejmujemy 1 przez indexy
        if j > 0 and K[(j-1) // 2] < K[k]:
            k = j // 2

        K[j], K[k] = K[k], K[j]

def move_down(K, i):
    k = i # pomocniczy index do znajdowania dzieci
    j = -1 # obecny index w liście
    while k != j:
        j = k
        # lewe dziecko
        if 2*j + 1 < len(K) and K[2 * j + 1] > K[k]:
            k = 2*j + 1
        # prawe dziecko
        if 2*j + 2 < len(K) and K[2*j + 2] > K[k]:
            k = 2*j + 2

        K[j], K[k] = K[k], K[j]

    return K

# K = [100, 20, 50, 1, 5, 6, 49]
# # change_elem(K, 1, 101)
# change_elem(K, 3, 1000)
# print(K)

# K = [1,100,3,4,5,6,78,9]
K = [1,2,3,4,5]
def build_heap(K):
    for i in range(len(K) // 2, -1, -1):
        move_down(K, i)
build_heap(K)
print(K)

def heapsort(K):
    build_heap(K)
    res = [K[0]]
    # idziemy z pętlą do przedostatniego elementu
    for i in range(len(K) - 1, 0, -1):
        K[0], K[i] = K[i], K[0]
        K = move_down(K[0:i], 0)
        res.insert(0, K[0])
    print(res)
# heapsort(K)
# print(K)
# priotity queues
# K = [100, 20, 50, 1, 5, 6, 49]
def del_max(K):
    K[0] = K[len(K) - 1]
    move_down(K, 0)

def insert(K, n):
    K.append(n)
    move_up(K, len(K) - 1)

# del_max(K)
# insert(K, 69)
# print(K)
