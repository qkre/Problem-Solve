from sys import stdin
from collections import deque
from heapq import heappop, heappush
input = stdin.readline
def dijkstra(start, distance, graph):
    heap = []
    heappush(heap, (0, start))
    distance[start] = 0


    while heap:
        cost, now = heappop(heap)

        if distance[now] < cost:
            continue

        for node in graph[now]:
            next_cost = cost + node[0]
            if next_cost < distance[node[1]]:
                distance[node[1]] = next_cost
                heappush(heap, (next_cost, node[1]))


def solution():
    N, M, X = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    reversed_graph = [[] for _ in range(N+1)]
    for _ in range(M):
        S, E, C = map(int, input().split())
        graph[S].append((C, E))
        reversed_graph[E].append((C, S))

    distance = [2e9 for _ in range(N+1)]
    reversed_distance = [2e9 for _ in range(N+1)]
    dijkstra(X, distance, graph)
    dijkstra(X, reversed_distance, reversed_graph)




    max_cost = 0

    for x, y in zip(distance[1:], reversed_distance[1:]):
        max_cost = max(max_cost, x+y)
    return max_cost


print(solution())