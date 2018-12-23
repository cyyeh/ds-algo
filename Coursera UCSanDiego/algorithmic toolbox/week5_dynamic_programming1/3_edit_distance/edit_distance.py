# Uses python3
def edit_distance(a, b):
    d = []
    
    for i in range(len(a) + 1):
        temp = []
        for j in range(len(b) + 1):
            if j == 0:
                temp.append(i)
            elif i == 0:
                temp.append(j)
            else:
                temp.append(None)
        d.append(temp)

    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            insertion = d[i][j-1] + 1
            deletion = d[i-1][j] + 1
            match = d[i-1][j-1]
            mismatch = d[i-1][j-1] + 1
            if a[i - 1] == b[j - 1]:
                d[i][j] = min(insertion, deletion, match)
            else:
                d[i][j] = min(insertion, deletion, mismatch)

    return d[len(a)][len(b)]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
