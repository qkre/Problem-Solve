from sys import stdin
from collections import deque
from copy import deepcopy

input = stdin.readline

def get_ices(maps, R, C, d):
    visited = [[False for _ in range(C)] for _ in range(R)]
    cnt = 0
    for r in range(R):
        for c in range(C):
            if maps[r][c] != 0 and not visited[r][c]:
                cnt += 1
                q = deque([(r, c)])
                visited[r][c] = True
                while q:
                    sr, sc = q.popleft()

                    for dr, dc in d:
                        nr, nc = dr + sr, dc + sc

                        if (0 <= nr < R and 0 <= nc < C) and maps[nr][nc] != 0 and not visited[nr][nc]:
                            visited[nr][nc] = True
                            q.append((nr, nc))

    return cnt

def solution():
    R, C = map(int, input().split())

    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    maps = [list(map(int, input().split())) for _ in range(R)]
    q = deque()
    for r in range(R):
        for c in range(C):
            if maps[r][c] != 0:
                q.append((r, c))

    valid = False
    ans = 0
    while q:
        if get_ices(maps, R, C, d) >= 2:
            valid = True
            break

        ans += 1
        new_maps = deepcopy(maps)
        water = []


        for _ in range(len(q)):
            r, c = q.popleft()
            cnt = 0

            for dr, dc in d:
                nr, nc = dr + r, dc + c

                if (0 <= nr < R and 0 <= nc < C) and maps[nr][nc] == 0:
                    cnt += 1
            if cnt > 0:
                if new_maps[r][c] - cnt > 0:
                    new_maps[r][c] -= cnt
                    q.append((r, c))

                else:
                    new_maps[r][c] = 0
                    water.append((r, c))

        for r, c in water:
            for dr, dc in d:
                nr, nc = dr + r, dc + c

                if (0<=nr<R and 0<=nc<C) and maps[nr][nc] != 0 and (nr,nc) not in q:
                    q.append((nr, nc))


        maps = new_maps

    if valid:
        print(ans)
    else:
        print(0)

solution()