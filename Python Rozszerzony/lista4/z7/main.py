board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def print_sudoku(board):
    for i in range(len(board)):
        # oddzielamy rzędy
        if i % 3 == 0 and i != 0:
            print("---------------------------")
        for j in range(len(board)):
            # oddzielamy kolumny
            if j % 3 == 0:
                print(" | ", end="")
            # dodajemy breakline na końcu, po 8 cyfrze
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

# znajdujemy 0 w danym rzędzie i kolumnie, zwracamy parę (rząd, kolumna) jak się udało
def find_spot(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j) # rząd, kolumna

    return None

# sprawdzenie czy sudoku jest ok
def is_valid(board, num, pos):
    # sprawdzenie rzędu
    # idziemy po kolei po rzędzie
    # sprawdzamy czy kolejne cyfry != num i unikamy sprawdzenie pozycji na którą obecnie wstawiamy
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and i != pos[1]:
            return False

    # sprawdzenie kolumny
    for i in range(len(board)):
        if board[i][pos[1]] == num and i != pos[0]:
            return False

    # sprawdzenie kwadratu
    # układ współrzędnych zaczyna się w lewym górnym rogu i y idą w dół a x w prawo
    square_x = pos[1] // 3
    square_y = pos[0] // 3
    for i in range(square_y * 3, square_y * 3 + 3):
        for j in range(square_x * 3, square_x * 3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False

    return True

def solve_sudoku(board):
    # dno rekursji
    if find_spot(board) is None:
        return board # udało się znaleźć rozwiązanie
    else:
        x,y = find_spot(board)
    for i in range(1, 10):
        # możemy dać liczbę na danej pozycji
        if is_valid(board, i, (x,y)):
            # podpinamy liczbę
            board[x][y] = i
            # sprawdzenie rekursji, czy działa
            if solve_sudoku(board) != None:
                return board
            # jak nie działa, podpinamy 0 i próbójemy od ostatniego 'i'
            board[x][y] = 0
    return None



if __name__ == '__main__':
    print_sudoku(board)
    solve_sudoku(board)
    print("------------------------------------")
    print_sudoku(board)
    # print(is_valid(board, 6, (0, 2)))
