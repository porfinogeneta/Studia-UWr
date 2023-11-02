from collections import deque


def find_path(labyrinth, start):
    width = len(labyrinth[0])
    height = len(labyrinth)

    # p = (x, y)
    def isCorrect(x, y):
        return 0 <= x < width and 0 <= y < height and labyrinth[x][y] != "X"

    visited = set()
    # kolejka przechowuje punkt w którym jesteśmy i ścieżkę do punktu
    # nowe ścieżki są dodawane na końcu kolejki
    queue = deque([(start, [])])

    while queue:

        (x, y), path = queue.popleft()

        if labyrinth[x][y] == 'E':
            return path

        for nx, ny in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            new_x = x + nx
            new_y = y + ny
            if isCorrect(new_x, new_y) and (new_x, new_y) not in visited:
                new_path = path + [(x, y)]  # nowa ścieżka, dla zaktualizowanej listy
                queue.append(((new_x, new_y), new_path))
                visited.add((new_x, new_y))
    # nie ma takiej ścieżki
    return None


if __name__ == '__main__':
    labyrinth = [
        [' ', 'X', ' ', ' ', ' '],
        [' ', 'X', 'X', 'X', ' '],
        [' ', ' ', ' ', ' ', ' '],
        ['X', 'X', 'X', ' ', ' '],
        [' ', ' ', ' ', ' ', 'E']]
    start = (0, 0)
    pth = find_path(labyrinth, start)
    # listy są na odwrót względem punktu x,y
    if pth:
        for x, y in pth:
            print(f"({y},{x})", end=" -> ")
        print("End")
    else:
        print("No path")
