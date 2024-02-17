from heapq import heappop, heappush

def solution(n, edge):

    graph = [[] for _ in range(n+1)]

    for s, e in edge:
        graph[s].append((e, 1))
        graph[e].append((s, 1))

    distance = [float('inf')] * (n+1)
    distance[1] = 0

    q = [(0, 1)] # (cost, node)

    while q:
        dist, node = heappop(q)

        for s, c in graph[node]:
            cost = dist + c

            if cost < distance[s]:
                distance[s] = cost
                heappush(q, (cost, s))

    while float('inf') in distance:
        distance.remove(float('inf'))

    return distance.count(max(distance))

print(solution(6,	[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))