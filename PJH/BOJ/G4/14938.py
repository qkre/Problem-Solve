from sys import stdin
from collections import defaultdict
from heapq import heappop, heappush
from collections import deque

input = stdin.readline

def dijkstra(start, N, graph):
    D = [float('inf')] * (N+1)
    D[start] = 0

    q = [(0, start)]

    while q:
        dist, now = heappop(q)

        if D[now] < dist:
            continue

        for next_node, next_dist in graph[now]:
            if dist + next_dist < D[next_node]:
                D[next_node] = dist + next_dist
                heappush(q, (dist + next_dist, next_node))

    return D
def solution():
    answer = 0
    N, M, R = map(int, input().split())

    items = [0] + list(map(int, input().split()))

    graph = defaultdict(list)

    for _ in range(R):
        a, b, l = map(int, input().split())

        graph[a].append((b, l))
        graph[b].append((a, l))

    for start in range(1, N+1):
        D = dijkstra(start, N, graph)
        tmp = 0
        for i in range(1, N+1):
            if D[i] <= M:
                tmp += items[i]

        answer = max(answer, tmp)


    return answer

print(solution())