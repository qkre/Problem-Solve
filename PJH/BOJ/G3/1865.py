import sys
input = sys.stdin.readline
INF = float('inf')


def bellmanford(start, edge, distance, N):
    edges = len(edge)

    distance[start] = 0

    for i in range(N+1):
        update = False
        for j in range(edges):
            start_node, next_node, cost = edge[j]

            if distance[start_node] + cost < distance[next_node]:
                update = True
                distance[next_node] = distance[start_node] + cost
                if i == N:
                    return True
        if not update:
            break

    return False


def solution():
    TC = int(input())

    for _ in range(TC):
        N, M, W = map(int, input().split())

        edge = []

        for _ in range(M):
            S, E, C = map(int, input().split())
            edge.append((S, E, C))
            edge.append((E, S, C))
        for _ in range(W):
            S, E, C = map(int, input().split())
            edge.append((S, E, -C))

        edge = list(set(edge))

        time_travel = False

        for i in range(1, N + 1):
            distance = [INF] * (N + 1)

            if bellmanford(i, edge, distance, N):
                time_travel = True
                break

        if time_travel:
            print("YES")
        else:
            print("NO")


solution()
