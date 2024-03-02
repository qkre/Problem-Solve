from sys import stdin
from collections import deque
from heapq import heappop, heappush
input = stdin.readline

N = int(input())
M = int(input())

graph = [[float('inf') for _ in range(N+1)] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)

def solution(N, M, graph):
    dijkstra = [[float('inf') for _ in range(N+1)] for _ in range(N+1)]

    for a in range(1, N+1):
        for b in  range(1, N+1):
            dijkstra[a][b] = graph[a][b]

    for a in range(1, N+1):
        for b in range(1, N+1):
            if a == b or graph[a][b] == float('inf'):
                continue

            q = [(graph[a][b], a, b)]


            while q:
                cost, s, e = heappop(q)

                for i in range(1, N+1):
                    if i == s or dijkstra[e][i] == float('inf'):
                        continue

                    ncost = dijkstra[e][i]

                    if cost + ncost < dijkstra[s][i]:
                        dijkstra[s][i] = cost + ncost
                        heappush(q, (cost+ncost, s, i))

    for y in range(1, N+1):
        for x in range(1, N +1):
            if y == x:
                print(0, end=' ')
            else:
                if dijkstra[y][x] == float('inf'):
                    print(0, end=' ')
                else:
                    print(dijkstra[y][x], end=' ')
        print()

solution(N, M, graph)