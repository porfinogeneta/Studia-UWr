import math

# zamiast iterować do 2^k interujemy do końca przedziału, wychodzi na to samo a prościej wartości funkcji znaleźć
def sumbis(a,b,h,f):
    # na początku wartość funkcji na krańcach przedziału
    res = 0.5*(f(a) + f(b))
    node = a + h
    while node < b:
        res += f(node) # przesuwamy się w przedziale
        node += h
    return res


def countIntegrals(a,b,M,f):
    K = 20 - M
    T = [0]*21
    # wyliczamy 20 wierszy bo tyle jest minimalnie
    for i in range(21):
        hk = (b-a)/(2**i)
        T[i] = hk*sumbis(a,b,hk,f)

    if M == 0:
        return T[K]

    # iteracja po kolumnach
    for m in range(1, 21):
        # iteracja po wierszach, idziemy w górę
        for k in range(20 - m,0,-1):
            # element w poprzedniej kolumnie na tym samym indeksie (+1 bo za zaczynamy przez -m od 19)
            T[k+1] = (math.pow(4, m) * T[k] - T[k+1]) / (math.pow(4,m) -1)
            if m == M and k == K:
                return T[m]

    return T[M]






