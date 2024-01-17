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
            print(m,k)
            if m == M and k == K:
                return T[m]

    return T[M]





# a,b - krańce przedziału, f - funkcja, m - liczba kolumn,

if __name__ == '__main__':
    f1 = lambda x: 2024 * math.pow(x, 8) - 1977 * math.pow(x, 4) - 1981
    f2 = lambda x: 1.0 / (1 + math.pow(x,2.0))
    f3 = lambda x: math.sin(5*x - math.pi/3)
    # dla 0 też z jakiegoś powodu dobrze zbiega (ostatni wiersz ma największy wpływ na oszacowanie, najczęściej go używamy)
    # result = countIntegrals(-3,2, 14, f1) # dopiero od 14 kolumny zaczyna sensownie zbiegać
    # result = countIntegrals(-3,3, 14, f2) # tutaj też od 14 kolumny
    result = countIntegrals(-3.0 * math.pi, math.pi/6.0, 15, f3) # tutaj od 15 kolumny
    print(result)

