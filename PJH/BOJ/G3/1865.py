import sys
from heapq import heappush, heappop

input = sys.stdin.readline
INF = sys.maxsize


def dijkstra(distance, graph, start):
    visited = [False] * len(distance)
    visited[start] = True
    distance[start] = 0

    heap = []
    heappush(heap, [0, start])

    while heap:
        cost, node = heappop(heap)

        if distance[node] < cost:
            continue

        for next_cost, next_node in graph[node]:
            if cost + next_cost < distance[next_node] and not visited[next_node]:
                visited[next_node] = True
                distance[next_node] = cost + next_cost
                heappush(heap, (cost + next_cost, next_node))


def solution():
    TC = int(input())

    for _ in range(TC):
        N, M, W = map(int, input().split())

        streets = [[] for _ in range(N + 1)]
        wormholes = [[] for _ in range(N + 1)]

        for _ in range(M):
            S, E, C = map(int, input().split())
            if S == E:
                continue
            streets[S].append((C, E))
            streets[E].append((C, S))

        for _ in range(W):
            S, E, C = map(int, input().split())
            if S == E:
                continue
            wormholes[S].append((-C, E))

        streets_distance = [[float('INF') for _ in range(N + 1)] for _ in range(N + 1)]
        wormholes_distance = [[float('INF') for _ in range(N + 1)] for _ in range(N + 1)]
        for i in range(1, N + 1):
            dijkstra(streets_distance[i], streets, i)
            dijkstra(wormholes_distance[i], wormholes, i)

        possible = False

        for i in range(1, N+1):
            for j in range(1, N+1):
                if i == j:
                    continue
                if wormholes_distance[i][j] < 0 and streets_distance[i][j] != float('INF'):
                    if streets_distance[i][j] + wormholes_distance[i][j] < 0:
                        possible = True
                        break
            if possible:
                break

        if possible:
            print("YES")
        else:
            print("NO")

solution()
