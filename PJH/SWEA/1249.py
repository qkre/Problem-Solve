import os
import sys
from check_answer import check_answer

current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"../input/{current_file}.txt", "r", encoding="utf-8-sig")

from heapq import heappop, heappush
result = []
T = int(input())

def dijkstra():
    heap = [(0, 0, 0)]
    min_maps = [[float("inf") for _ in range(N)] for _ in range(N)]
    min_maps[0][0] = 0
    while heap:
        cost, r, c = heappop(heap)

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc

            if 0 <= nr < N and 0 <= nc < N:
                ncost = cost + maps[nr][nc]
                if ncost < min_maps[nr][nc]:
                    min_maps[nr][nc] = ncost
                    heappush(heap, (ncost, nr, nc))

    return min_maps[-1][-1]
for case in range(1, T + 1):
    ans = 0
    N = int(input())

    maps = [list(map(int, list(input()))) for _ in range(N)]

    ans = dijkstra()


    result.append(f"#{case} {ans}")

for r in result:
    print(r)

check_answer(current_file, result)
