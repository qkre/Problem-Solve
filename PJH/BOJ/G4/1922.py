from sys import stdin
from collections import deque
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

    if a != b:
        if a < b:
            root[b] = a
        else:
            root[a] = b

def solution():
    N = int(input())
    M = int(input())

    edges = []
    root = [i for i in range(N + 1)]

    for _ in range(M):
        edges.append(tuple(map(int, input().split())))

    edges.sort(key=lambda x: x[2])
    edges = deque(edges)
    cnt = 0
    answer = 0

    while cnt < N-1:
        S, E, C = edges.popleft()

        if find(root, S) == find(root, E):
            continue

        union(root, S, E)
        cnt += 1
        answer += C

    print(answer)

solution()