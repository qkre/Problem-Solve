from sys import stdin
from collections import deque
from copy import deepcopy

input = stdin.readline

D = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def is_outside(air, maps, N, M, q):
    while q:
        r, c = q.popleft()

        for dr, dc in D:
            nr, nc = r + dr, c + dc

            if (0 <= nr < N and 0 <= nc < M) and not air[nr][nc] and maps[nr][nc] == 0:
                air[nr][nc] = True
                q.append((nr, nc))

def melt_cheese(air, maps, N, M):

    new_maps = deepcopy(maps)

    air_pockets = deque()

    for r in range(N):
        for c in range(M):
            if maps[r][c] == 1:
                cnt = 0
                for dr, dc in D:
                    nr, nc = r + dr, c + dc

                    if (0 <= nr < N and 0 <= nc < M) and air[nr][nc] and maps[nr][nc] == 0:
                        cnt += 1

                if cnt >= 2:
                    new_maps[r][c] = 0
                    air[r][c] = True
                    air_pockets.append((r, c))

    is_outside(air, new_maps, N, M, air_pockets)

    return new_maps

def is_cheese(maps):
    for m in maps:
        if 1 in m:
            return True

    return False

def solution():
    N, M = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(N)]
    air = [[False for _ in range(M)] for _ in range(N)]
    is_outside(air, maps, N, M, deque([(0, 0)]))

    answer = 0

    while is_cheese(maps):
        answer += 1
        maps = melt_cheese(air, maps, N, M)


    return answer

print(solution())
