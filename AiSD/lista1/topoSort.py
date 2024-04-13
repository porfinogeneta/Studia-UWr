def topoSort(graph):
    visited = [False] * len(graph)
    sorted = []
    for v in graph.keys():
        if not visited[v-1]:
            visit(v, visited, sorted, graph)

    return sorted

def visit(v, visited, sorted, graph):
    if visited[v-1]: return

    visited[v-1] = True

    sorted.append(v)

    for u in graph[v]:
        if not visited[u-1]:
            visit(u, visited, sorted, graph)


if __name__ == '__main__':
    g = {1: [2,4], 2:[3], 3:[], 4:[5,6], 5:[], 6:[7], 7:[]}
    print(topoSort(g))