def superSeq(str1, str2):
    m = len(str1)
    n = len(str2)

    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):

            if i == 0:
                dp[i][j] = j  # dla pustego str1 kolejne długości to kolejne znaki str2

            elif j == 0:
                dp[i][j] = i

            elif str1[i - 1] == str2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]  # szukamy najbardziej korzystnego rozwiązania bez ostanich
            else:
                # badamy które rozwiązanie jest bardziej korzystne,
                # to bez ostatniej litery w str1 czy to bez ostatniej w str2
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1])

    def getSeq(col, row):
        res = ""

        while row > 0 and col > 0:
            if str1[col - 1] == str2[row - 1]:
                res += str1[col - 1]
                row -= 1
                col -= 1
            # poprzednia kolumna ma większy wynik, to z niej przyszliśmy
            elif dp[row][col - 1] > dp[row - 1][col]:
                res += str1[col - 1]
                col -= 1
            else:
                res += str2[row - 1]
                row -= 1

        if row > 0:
            res = res + str1[:col]
        if col > 0:
            res = res + str2[:row]

        return res

    return dp[m][n], getSeq(m, n)


if __name__ == "__main__":
    X = "AXTAB"
    Y = "XTXAYB"
    print(superSeq(X, Y))
