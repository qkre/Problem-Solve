from sys import stdin
from collections import deque

input = stdin.readline

def solution():
    N = int(input())
    graph = [[0 for _ in range(N)] for _ in range(N)]
    arr = [list(map(int, input().split())) for _ in range(N)]

    for s in range(N):
        for e in range(N):
            if arr[s][e] == 1:
                graph[s][e] = 1

    q = deque()

    for s in range(N):
        visited = [[False for _ in range(N)] for _ in range(N)]
        for e in range(N):
            if graph[s][e] == 1:
                q.append((s, s, e))
                while q:
                    init, start, end = q.popleft()

                    for i in range(N):
                        if graph[end][i] == 1 and not visited[end][i]:
                            graph[init][i] = 1
                            visited[end][i] = True

                            q.append((init, end, i))

    for g in graph:
        print(*g)

solution()
