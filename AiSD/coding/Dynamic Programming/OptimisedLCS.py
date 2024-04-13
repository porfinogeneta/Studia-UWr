
def optLCS(str1, str2):
    m = len(str1)pm
    n= len(str2)
    dp = [0 for _ in range(n+1)]

    for i in range(1, m+1):
        prevRowPrevCol = 0 # zaczynamy iterację, domyślna wartość po przekątnej to 0
        for j in range(1, n+1):
            prevRow = dp[j] # poprzedni rząd, to wartość nadpisywana
            if str1[i-1] == str2[j-1]:
                dp[j] = prevRowPrevCol + 1 # dodajemy 1 do elementu po przekątnej
            else:
                dp[j] = max(dp[j-1], prevRow)
            # po każdej iteracji przesuwamy się w prawo, czyli prevRow przechodzi nam na prevRowPrevCol
            prevRowPrevCol = prevRow

    return dp

if __name__ == "__main__":
    X = "AGGTAB"
    Y = "GXTXAYB"
    print(optLCS(X, Y))