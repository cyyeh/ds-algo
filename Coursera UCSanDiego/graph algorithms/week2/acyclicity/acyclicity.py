#Uses python3

import sys


def acyclic(adj):
    def explore(v):
        visited[v] = True
        if adj[v]:
            for w in adj[v]:
                if not visited[w]:
                    vertices.append(w)
                    explore(w)
        else:
            vertices.append(v)

    vertices = []
    visited = [False for _ in range(len(adj))]

    for v in range(len(adj)):
        if not visited[v]:
            explore(v)    

    print(vertices)

    return 0 if len(vertices) + 1 == len(adj) else 1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))