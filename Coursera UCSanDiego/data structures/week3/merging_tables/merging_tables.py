# python3

import sys

n, m = map(int, sys.stdin.readline().split())
lines = list(map(int, sys.stdin.readline().split()))
rank = [1] * n
parent = list(range(0, n))
ans = max(lines)

def getParent(table):
    # find parent and compress path
    if table != parent[table]:
        parent[table] = getParent(parent[table])
    return parent[table]

def merge(destination, source, ans):
    realDestination = getParent(destination)
    realSource = getParent(source)

    if realDestination == realSource:
        return False, ans

    # merge two components
    # use union by rank heuristic 
    # update ans with the new maximum table size
    if rank[realDestination] > rank[realSource]:
        parent[realSource] = realDestination
        if lines[realSource] > 0:
            lines[realDestination] += lines[realSource]
            lines[realSource] = 0      
            ans = lines[realDestination] if lines[realDestination] > ans else ans 
    elif rank[realDestination] < rank[realSource]:
        parent[realDestination] = realSource
        if lines[realDestination] > 0:
            lines[realSource] += lines[realDestination]
            lines[realDestination] = 0
            ans = lines[realSource] if lines[realSource] > ans else ans 
    else:
        parent[realSource] = realDestination 
        rank[realDestination] += 1

        if lines[realSource] > 0:
            lines[realDestination] += lines[realSource]
            lines[realSource] = 0
            ans = lines[realDestination] if lines[realDestination] > ans else ans 

    return True, ans

for i in range(m):
    destination, source = map(int, sys.stdin.readline().split())
    _, ans = merge(destination - 1, source - 1, ans)
    print(ans)
    
