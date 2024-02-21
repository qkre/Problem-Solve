from sys import stdin
from heapq import heappush, heappop

input = stdin.readline


def dijkstar(start, graph, distance):
    visited = [False] * len(distance)
    distance[start] = 0
    visited[start] = True

    heap = []
    heappush(heap, (0, start))

    while heap:
        cost, node = heappop(heap)

        if distance[node] < cost:
            continue

        for branch in graph[node]:
            next_cost = cost + branch[0]
            next_node = branch[1]

            if next_cost < distance[next_node] and not visited[next_node]:
                distance[next_node] = next_cost
                heappush(heap, (next_cost, next_node))


def solution():
    N, E = map(int, input().split())
    graph = [[] for _ in range(N + 1)]

    for _ in range(E):
        S, E, C = map(int, input().split())
        graph[S].append((C, E))
        graph[E].append((C, S))

    V1, V2 = map(int, input().split())

    distance_1 =[2e9] * (N+1)
    distance_V1 = [2e9] * (N+1)
    distance_V2 = [2e9] * (N+1)

    dijkstar(1, graph, distance_1)
    dijkstar(V1, graph, distance_V1)
    dijkstar(V2, graph, distance_V2)


    answer = min(distance_1[V1] + distance_V1[V2] + distance_V2[N],
                 distance_1[V2] + distance_V2[V1] + distance_V1[N])
    if answer >= 2e9:
        answer = -1

    return answer

print(solution())
