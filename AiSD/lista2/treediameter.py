def treeDFS(T, v, visited, counter):

    if visited[v]:
        return tuple(counter, v)

    visited[v] = True

    longest_paths = []
    for w in T[v]:
        if not visited[w]:
            longest_paths.append(treeDFS(T, w, visited, counter + 1))
    if longest_paths:
        return max(longest_paths, key=lambda t: t[0])
    else:
        return (counter,v)

def treeDiameter(T):
    visited = [False] * len(G)
    # puszczamy dfs dla losowego wierzchołka v
    length,v = treeDFS(T, 4, visited, 0)
    visited = [False] * len(G)
    # z v szukamy najbardziej oddalonego wierzchołka
    diameter,end = treeDFS(T, v, visited, 0)
    return (v, diameter, end)



if __name__ == "__main__":
    G = {0: [1,2], 1: [0,3], 2: [0,4], 3: [1], 4: [2,5,6,7], 5:[4,8], 6: [4], 7:[4], 8:[5]}
    print(treeDiameter(G))