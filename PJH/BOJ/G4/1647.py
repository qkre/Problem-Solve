from sys import stdin

input = stdin.readline

def find(root, v):
    if root[v] == v:
        return v
    else:
        root[v] = find(root, root[v])
        return root[v]

def union(root, a, b):
    a = find(root, a)
    b = find(root, b)

    if a < b:
        root[b] = a
    else:
        root[a] = b

def cities(root):
    return len(list(set(root[1:])))
def solution():
    N, M = map(int, input().split())
    root = [i for i in range(N + 1)]
    edges = [tuple(map(int, input().split())) for _ in range(M)]
    edges.sort(key=lambda x: x[2], reverse=True)

    cnt = 0
    answer = 0

    minimum_edges = []

    while cnt < N-1:
        S, E, C = edges.pop()

        if find(root, S) == find(root, E):
            continue

        union(root, S, E)
        cnt += 1
        minimum_edges.append((S, E, C))

    minimum_edges.pop()

    for S, E, C in minimum_edges:
        answer += C

    print(answer)

solution()
