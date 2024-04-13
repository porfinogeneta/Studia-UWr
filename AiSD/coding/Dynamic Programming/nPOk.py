

def nPOk(n, k):
    # uzupełniamy pierwszą kolumnę (dla 0) 1 oraz całą przekątną 1 (l po l)
    tab = [[1 if r == c or r == 0 else 0 for r in range(k+1)] for c in range(n+1)]
    for j in range(1,k+1):
        for i in range(j+1, n+1):
            # dla j kolumny i i tego wiersza element to
            # ta sama kolumna poprzedni wiersz + poprzedni wiersz i poprzedni kolumna
            tab[i][j] = tab[i-1][j] + tab[i-1][j-1]

    return tab[n][k]


if __name__ == "__main__":
    print(nPOk(5,2))