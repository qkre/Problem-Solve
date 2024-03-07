from sys import stdin
from heapq import heappop, heappush, heapify
from collections import defaultdict

input = stdin.readline

def solution():
    N = int(input())
    M = int(input())

    graph = defaultdict(list)

    for _ in range(M):
        S, E, C = map(int, input().split())

        graph[S].append((E, C))

    S_target, E_target = map(int, input().split())

    if S_target == E_target:
        print(0)
        print(1)
        print(1)
        return

    q = []
    dijkstra = [float('inf')] * (N+1)

    answer = []

    for end_node, cost in graph[S_target]:
        dijkstra[end_node] = min(dijkstra[end_node], cost)
        heappush(q, (cost, S_target, end_node, [S_target, end_node]))


    while q:
        cost, start_node, end_node, path = heappop(q)

        if end_node == E_target and cost == dijkstra[end_node]:
            answer = path.copy()
            break

        for new_node, new_cost in graph[end_node]:
            next_cost = cost + new_cost

            if next_cost < dijkstra[new_node]:
                dijkstra[new_node] = next_cost
                new_path = path.copy()
                new_path.append(new_node)
                heappush(q, (next_cost, end_node, new_node, new_path))

    print(dijkstra[E_target])
    print(len(answer))
    print(*answer)

solution()