from sys import stdin
from collections import deque
input = stdin.readline

def bfs(q, max_node, max_cost, tree, visited):
    while q:
        node, cost = q.popleft()
        if max_cost < cost:
            max_node = node
            max_cost = cost

        for new_node, new_cost in tree[node]:
            if not visited[new_node]:
                visited[new_node] = True
                q.append((new_node, cost + new_cost))

    return max_node, max_cost

def solution():
    N = int(input())

    tree = [[] for _ in range(N + 1)]

    for _ in range(1, N):
        start, end, cost = map(int, input().split())
        tree[start].append((end, cost))
        tree[end].append((start, cost))

    max_node = 0
    max_cost = 0

    q = deque([(1, 0)])
    visited = [False] * (N + 1)
    visited[1] = True

    max_node, max_cost = bfs(q, max_node, max_cost, tree, visited)

    q = deque([(max_node, 0)])
    visited = [False] * (N+1)
    visited[max_node] = True

    max_node, max_cost = bfs(q, max_node, max_cost, tree, visited)

    print(max_cost)

solution()
