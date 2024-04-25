

# pojemnność plecaka, lista rzeczy (value,weight)
def knapsack(capacity, stuff):
    # tablica dwuwymiarowa - kolumny to kolejne wagi do uzupełnienia,
    # wiersze to kolejne rzeczy do sprawdzenia
    dp = [[0 for _ in range(capacity + 1)] for _ in range(len(stuff) + 1)]
    # algorytm działa na takiej zasadzie, że w każdej komórce pytamy się,
    # czy mogę wziąć ten element, jeśli tak, to czy jak go wezmę uzyskam wartość większą
    # niż tą, która tem teraz jest, jeśli tak to zamieniam
    for i in range(1, len(stuff) + 1):
        for j in range(1, capacity + 1):
            # jak taką wagę zmieścimy w plecaku
            if j - stuff[i - 1][1] >= 0:
                # maksimum z wartości, która już poprzednio została spakowana, dotychczas najlepsza
                # i tego jak byśmy wzięli dany przedmiot, jak go weźmiemy to wybierzemy też
                # dla mniejszej wagi najkorzystniejsze rozwiązanie z poprzedniego rzędu
                dp[i][j] = max(dp[i-1][j], stuff[i-1][0] + dp[i-1][j-stuff[i-1][1]])

    return dp

# chcemy się dowiedzieć jakie rzeczy utworzyły nam dp
# w tym celu zaczynamy w prawym dolnym rogu i jeżeli wartość tam jest taka sama jak
# wyżej to oznacza, że użyliśmy poprzedniej rzeczy, jak jest inna
# to użyliśmy rzeczy z danego wiersza oraz drugiej rzeczy z poprzedniego wiersza, która
# dopełniła nam wagę
def getStuff(dp, capacity, stuff):
    res = []
    stuffCount = len(stuff)
    while capacity > 0 and dp[stuffCount][capacity] != 0:
        # jeśli użyliśmy aktualnej rzeczy, to liczba aktualnie sprawdzana
        # jest większa od tej powyżej niej, nie przepisaliśmy wartości
        if dp[stuffCount][capacity] > dp[stuffCount - 1][capacity]:
            res.append(stuff[stuffCount - 1])
            # cofamy się na przedmiot o odpowiedniej wadze
            capacity -= stuff[stuffCount - 1][1]
        stuffCount -= 1

    return res

if __name__ == "__main__":
    capacity = 7
    stuff = [(5,4), (2,3), (3,2), (4,3), (2,1)]
    dp = knapsack(capacity, stuff)
    getStuff(dp, capacity, stuff)