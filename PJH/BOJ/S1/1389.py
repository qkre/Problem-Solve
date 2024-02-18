from sys import stdin
from heapq import heappop, heappush
from collections import deque

input = stdin.readline


def bfs(graph, start):
    num = [0] * (N + 1)
    visited = [False] * (N + 1)
    visited[start] = True
    q = deque()
    q.append(start)

    while q:
        end = q.popleft()
        for i in graph[end]:
            if not visited[i] or num[end] + 1 < num[i]:
                q.append(i)
                num[i] = num[end] + 1
                visited[i] = True

    return sum(num)

def solution(N, M, arr):
    graph = [[] for _ in range(N + 1)]
    bacon = []
    for A, B in arr:
        graph[A].append(B)
        graph[B].append(A)


    for i in range(1, N+1):
        if graph[i]:
            bacon.append(bfs(graph, i))

    return bacon.index(min(bacon)) + 1

N, M = map(int, input().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(M)]

print(solution(N, M, arr))
