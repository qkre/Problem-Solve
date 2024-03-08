from sys import stdin
from collections import deque
from copy import deepcopy
from itertools import combinations
input = stdin.readline

def install_walls(maps, w1, w2, w3, virus, N, M):
    new_maps = deepcopy(maps)

    for r, c in [w1, w2, w3]:
        new_maps[r][c] = 1

    while virus:
        r, c = virus.popleft()

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc

            if (0 <= nr < N and 0 <= nc < M) and new_maps[nr][nc] == 0:
                new_maps[nr][nc] = 2
                virus.append((nr, nc))

    answer = 0

    for r in range(N):
        for c in range(M):
            if new_maps[r][c] == 0:
                answer += 1

    return answer


def solution():
    N, M = map(int, input().split())

    maps = [list(map(int, input().split())) for _ in range(N)]

    walls = []
    virus = deque()
    for r in range(N):
        for c in range(M):
            if maps[r][c] == 0:
                walls.append((r, c))
            elif maps[r][c] == 2:
                virus.append((r, c))



    combs = list(combinations(walls, 3))
    cnt = 0
    for comb in combs:
        w1, w2, w3 = comb

        cnt = max(cnt, install_walls(maps, w1, w2, w3, virus.copy(), N, M))

    print(cnt)

solution()