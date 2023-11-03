def primes_imperative(n):
    res = []
    # początek algorytmu sita Eratostenesa, tablica, z której będziemy 'wykreślać' liczby
    primes = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if primes[p] == True:
            # zaczynamy od kwadratu danej liczby pierwszej, licznik idzie o kolejne wielokrontości p
            for i in range(p*p, n+1, p):
                primes[i] = False
        p += 1

    for i in range(2, len(primes)):
        if primes[i]:
            res.append(i)
    return res

def primes_comprehension(n):
    # bierzemy kolejne liczby p i sprawdzamy czy nie są podzielne przez żadną liczbę od 2 do swojego pierwiastka kwadratowego
    # all sprawia że sprawdzenie modulo jest zastosowane dla każdej drugiej iteracji
    return [p for p in range(2, n) if all(p % i != 0 for i in range(2, int(p**(0.5)) + 1))]


def primes_functional(n):

    def is_prime(i):
        if i == 2:
            return True
        # sprawdzamy do pierwiastka i badamy czy to nie ta sama liczba
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                return False
        return True

    res = [i for i in range(2, n+1)]
    return list(filter(is_prime, res))

import timeit
if __name__ == '__main__':
    table = []
    for i in range(10, 100, 10):
        exec_imperative = timeit.timeit(f'primes_imperative({i})', globals=globals(), number=1)
        exec_comprehension = timeit.timeit(f'primes_comprehension({i})', globals=globals(), number=1)
        exec_functional = timeit.timeit(f'primes_functional({i})', globals=globals(), number=1)
        table.append([i, exec_imperative, exec_comprehension, exec_functional])

    print('| {:^3} | {:^10} | {:^10} | {:^10} |'.format("n", "imperative", "comprehe", "functional"))
    for row in table:
        print('| {:^3} | {:^.4e} | {:^.4e} | {:^.4e} |'.format(*row))
    # print(primes_imperative(20))
    # print(primes_comprehension(20))
    # print(primes_functional(20))
