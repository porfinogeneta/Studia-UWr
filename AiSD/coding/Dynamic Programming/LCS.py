


def LCS(X, Y):
    # tworzymy tablicę z zerami na pierwszej kolumnie i pierwszym wierszu
    m = len(X)
    n = len(Y)
    tab = [[0 for _ in range(n+1)] for _ in range(m+1)]
    # porównujemy każdy znak z X, z każdym znakiem z Y
    # w razie ich różności bierzemy maksymalny ciąg utworzony, bez aktualnie
    # analizowanego znaku z X lub bez aktualnie analizowanego z Y
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                # jak są równe bierzemy długość ciągu z oboma literami poprzednimi,
                # element po przekątnej
                tab[i][j] = tab[i-1][j-1] + 1
            else:
                # bierzemy maksimum bez ostanich liter z X i Y
                tab[i][j] = max(tab[i-1][j], tab[i][j-1])

    return tab


# aby znaleźć maksymalną sekwencję postępujemy następująco
# na kolejnych elementach tablicy, poczynając od n,m szukamy maksimum
# w poprzedniej kolumnie i tym samym wierszu, tej samej kolumnie i poprzednim wierszu i na aktualnej
# pozycji
def getPath(X, tab, m, n):
    # koniec tablicy, zwracamy pusty string
    if m == 0 or n == 0:
        return ""
    # obecny element jest maksymalny, czyli ta litera musiała być obecna w obu stringach
    if tab[m][n] > tab[m][n-1] and tab[m][n] > tab[m-1][n]:
        return getPath(X, tab, m-1, n-1) + X[m-1]
    # element w poprzednim wierszu i tej samej kolumnie jest nawiększy, wybieramy ten element
    if tab[m-1][n] >= tab[m][n-1] and tab[m-1][n] >= tab[m][n]:
        return "" + getPath(X, tab, m-1, n)
    # element w tym samym wierszu, ale poprzedniej kolumnie jest największy, wybieramy ten element
    if tab[m][n-1] >= tab[m][n] and tab[m][n-1] >= tab[m-1][n]:
        return "" + getPath(X, tab, m, n-1)

if __name__ == "__main__":
    X = "acdbxbab"
    Y = "wadgbfffaabab"
    tab = LCS(X, Y)
    print(tab)
    print(getPath(X, tab, len(X), len(Y)))
