from sys import stdin
from copy import deepcopy

input = stdin.readline


def diffusion(R, C, maps, air_up, air_down):
    new_maps = [[0 for _ in range(C)] for _ in range(R)]
    new_maps[air_up[0]][air_down[1]] = -1
    new_maps[air_down[0]][air_down[1]] = -1

    for r in range(R):
        for c in range(C):
            if maps[r][c] > 0:
                cnt = 0
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < R and 0 <= nc < C and maps[nr][nc] != -1:
                        new_maps[nr][nc] += maps[r][c] // 5
                        cnt += 1
                new_maps[r][c] += maps[r][c] - (maps[r][c] // 5 * cnt)

    return new_maps


def move_air_up(R, C, maps, air_up):
    sr, sc = air_up
    new_maps = deepcopy(maps)
    # right
    for c in range(C - 1, 0, -1):
        if c > 1:
            new_maps[sr][c] = maps[sr][c - 1]
        else:
            new_maps[sr][c] = 0

    # up
    for r in range(0, sr):
        new_maps[r][-1] = maps[r + 1][-1]

    # left
    for c in range(C - 1):
        new_maps[0][c] = maps[0][c + 1]

    # down
    for r in range(sr - 1 , 0, -1):
        new_maps[r][0] = maps[r - 1][0]

    return new_maps


def move_air_down(R, C, maps, air_down):
    sr, sc = air_down
    new_maps = deepcopy(maps)

    # right
    for c in range(C - 1, 0, -1):
        if c > 1:
            new_maps[sr][c] = maps[sr][c - 1]
        else:
            new_maps[sr][c] = 0

    # down
    for r in range(sr + 1, R):
        new_maps[r][-1] = maps[r - 1][-1]

    # left
    for c in range(C - 1):
        new_maps[-1][c] = maps[-1][c + 1]

    # up
    for r in range(R - 2, sr, -1):
        new_maps[r][0] = maps[r + 1][0]

    return new_maps
def solution():
    R, C, T = map(int, input().split())

    maps = [list(map(int, input().split())) for _ in range(R)]

    air_up = ()
    air_down = ()

    for r in range(R):
        for c in range(C):
            if maps[r][c] == -1:
                if not air_up:
                    air_up = (r, c)
                else:
                    air_down = (r, c)
        if air_up and air_down:
            break

    for time in range(T):
        maps = diffusion(R, C, maps, air_up, air_down)
        maps = move_air_up(R, C, maps, air_up)
        maps = move_air_down(R, C, maps, air_down)

    answer = 2
    for _ in maps:
        answer += sum(_)

    print(answer)
solution()
