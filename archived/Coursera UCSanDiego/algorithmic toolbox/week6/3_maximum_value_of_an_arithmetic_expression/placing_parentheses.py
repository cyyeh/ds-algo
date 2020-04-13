# Uses python3
import math

def get_maximum_value(dataset):
    def evalt(a, b, op):
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        else:
            assert False

    def min_and_max(i, j):
        current_min = 100000
        current_max = -100000
        for k in range(i, j):
            a = evalt(M[i][k], M[k+1][j], dataset[i+1])
            b = evalt(M[i][k], m[k+1][j], dataset[i+1])
            c = evalt(m[i][k], M[k+1][j], dataset[i+1])
            d = evalt(m[i][k], m[k+1][j], dataset[i+1])
            current_min = min(current_min, a, b, c, d)
            current_max = max(current_max, a, b, c, d)
        return (current_min, current_max)
    
    M = []
    m = []
    for i in range(math.ceil(len(dataset)/2)):
        temp = []
        for j in range(math.ceil(len(dataset)/2)):
            if i == j:
                temp.append(int(dataset[i * 2]))
            else:
                temp.append(None)
        M.append(temp)
        m.append(temp)


    for s in range(1, len(dataset)):
        for i in range(len(dataset)-s-1):
            j = i + s
            m[i][j], M[i][j] = min_and_max(i, j)
    
    print(M)

    return M[0][math.ceil(len(dataset)/2)-1]


if __name__ == "__main__":
    print(get_maximum_value(input()))
