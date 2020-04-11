# Uses python3
import sys

def optimal_weight(W, w):
    T = [[None] * (len(w) + 1) for _ in range(W + 1)]

    for u in range(W + 1):
        T[u][0] = 0

    for i in range(1, len(w) + 1):
        for u in range(W + 1):
            T[u][i] = T[u][i - 1]
            if u >= w[i - 1]:
                T[u][i] = max(T[u][i], T[u - w[i - 1]][i - 1] + w[i - 1])

    return T[W][len(w)]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
