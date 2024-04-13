# funkcja do znalezienie najkrótszego cycklu w grafie nieskierowanym
# bez wag, zwraca True jeśli udało się dojść do końca alternatyną ścieżką,
# wpp. zwraca False
def BFS_has_cycle(self, start, end):
    visited = [False] * (max(self.graph) + 1)
    queue = []
    queue.append(start)
    visited[start] = True

    while queue:

        s = queue.pop(0)

        for i in self.graph[s]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                if i == end:
                    return True

    return False




