from collections import defaultdict
from heapq import heappop, heappush


def solution(n, paths, gates, summits):

    graph = defaultdict(set)

    for i, j, w in paths:
        graph[i].add((j, w))
        graph[j].add((i, w))


    intensities = [float('inf')] * (n+1)
    heap = []

    for gate in gates:
        intensities[gate] = 0
        heappush(heap, (0, gate))

    while heap:
        intensity, node = heappop(heap)

        if intensities[node] < intensity  or node in summits:
            continue

        for neighbor, weight in graph[node]:
            next_intensity = max(intensity, weight)

            if next_intensity < intensities[neighbor]:
                intensities[neighbor] = next_intensity
                heappush(heap, (next_intensity, neighbor))

    answer = [-1, float('inf')]

    summits = set(summits)

    for summit in summits:
        if intensities[summit] < answer[1]:
            answer = [summit, intensities[summit]]

    print(answer)
    return answer


solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5])
solution(7, [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]], [1], [2, 3, 4])
