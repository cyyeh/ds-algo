# Uses python3

def optimal_summands(n):
    summands = []

    if n <= 2:
        summands.append(n)
    else:
        i = 1
        while n > 0:
            if n - i != i and (not len(summands) or n - i > summands[-1]):
                summands.append(i)
                n -= i
                i += 1
            else:
                summands.append(n)
                break
            
    return summands

if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
