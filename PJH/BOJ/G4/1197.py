from sys import stdin
from collections import deque
from heapq import heappop, heappush

input = stdin.readline

def find(root, v):
    if v == root[v]:
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
    V, E = map(int, input().split())
    answer = 0
    root = [i for i in range(V + 1)]
    edges = []

    for _ in range(E):
        s, e, c = map(int, input().split())

        edges.append((s, e, c))

    edges.sort(key=lambda x: x[2])
    edges = deque(edges)
    cnt = 0
    while cnt < V-1:
        start, end, cost = edges.popleft()

        if find(root, start) != find(root, end):
            union(root, start, end)
            cnt += 1
            answer += cost

    print(answer)


solution()
