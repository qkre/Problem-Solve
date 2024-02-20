from sys import stdin
from collections import deque

input = stdin.readline


def solution():
    V = int(input())
    tree = [[] for _ in range(V + 1)]
    for _ in range(V):
        arr = list(map(int, input().split()))
        S = arr[0]
        arr = arr[1:-1]
        for i in range(0, len(arr) - 1, 2):
            tree[S].append((arr[i], arr[i + 1]))

    max_node = 0
    max_cost = 0
    visited = [False] * (V+1)
    visited[1] = True
    q = deque([(1, 0)])
    while q:
        S, cost = q.popleft()
        if max_cost < cost:
            max_cost = cost
            max_node = S

        for branch in tree[S]:
            if not visited[branch[0]]:
                visited[branch[0]] = True
                q.append((branch[0], cost+branch[1]))

    q = deque([(max_node, 0)])
    visited = [False] * (V + 1)
    visited[max_node] = True
    while q:
        S, cost = q.popleft()
        if max_cost < cost:
            max_cost = cost

        for branch in tree[S]:
            if not visited[branch[0]]:
                visited[branch[0]] = True
                q.append((branch[0], cost + branch[1]))

    print(max_cost)


solution()
