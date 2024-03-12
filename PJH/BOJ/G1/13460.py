from sys import stdin
from collections import deque
from copy import deepcopy

input = stdin.readline
escaped = False
possible = True


def get_pos(maps, N, M):
    BB = (0, 0)
    BR = (0, 0)
    HOLE = (0, 0)
    for r in range(N):
        for c in range(M):
            if maps[r][c] == 'B':
                BB = (r, c)
            if maps[r][c] == 'R':
                BR = (r, c)
            if maps[r][c] == 'O':
                HOLE = (r, c)

    return [BR, BB, HOLE]


def move_up(maps, N, M):
    global escaped, possible
    possible = True
    new_maps = deepcopy(maps)

    BR, BB, HOLE = get_pos(maps, N, M)

    def move_red():
        global escaped
        # 빨간공 움직이기
        BR_r, BR_c = BR

        for r in range(BR_r, 0, -1):
            if new_maps[r - 1][BR_c] == '.':
                new_maps[r - 1][BR_c] = 'R'
                new_maps[r][BR_c] = '.'
            elif new_maps[r - 1][BR_c] == 'O':
                new_maps[r][BR_c] = '.'
                escaped = True
                break
            else:
                break

    def move_blue():
        global escaped, possible
        # 파란공 움직이기
        BB_r, BB_c = BB

        for r in range(BB_r, 0, -1):
            if new_maps[r - 1][BB_c] == '.':
                new_maps[r - 1][BB_c] = 'B'
                new_maps[r][BB_c] = '.'
            elif new_maps[r - 1][BB_c] == 'O':
                new_maps[r][BB_c] = '.'
                escaped = False
                possible = False
                break
            else:
                break

    if BR[1] == BB[1]:
        if BR[0] > BB[0]:
            move_blue()
            if possible:
                move_red()
        else:
            move_red()
            move_blue()
    else:
        move_red()
        move_blue()

    return new_maps


def move_down(maps, N, M):
    global escaped, possible

    possible = True
    new_maps = deepcopy(maps)

    BR, BB, HOLE = get_pos(maps, N, M)

    def move_red():
        global escaped
        BR_r, BR_c = BR

        for r in range(BR_r, N - 1):
            if new_maps[r + 1][BR_c] == '.':
                new_maps[r + 1][BR_c] = 'R'
                new_maps[r][BR_c] = '.'
            elif new_maps[r + 1][BR_c] == 'O':
                new_maps[r][BR_c] = '.'
                escaped = True
                break
            else:
                break

    def move_blue():
        global escaped, possible
        BB_r, BB_c = BB

        for r in range(BB_r, N - 1):
            if new_maps[r + 1][BB_c] == '.':
                new_maps[r + 1][BB_c] = 'B'
                new_maps[r][BB_c] = '.'
            elif new_maps[r + 1][BB_c] == 'O':
                new_maps[r][BB_c] = '.'
                escaped = False
                possible = False
                break
            else:
                break

    if BR[1] == BB[1]:
        if BR[0] < BB[0]:
            move_blue()
            if possible:
                move_red()
        else:
            move_red()
            move_blue()
    else:
        move_red()
        move_blue()

    return new_maps


def move_left(maps, N, M):
    global escaped, possible
    possible = True
    new_maps = deepcopy(maps)

    BR, BB, HOLE = get_pos(maps, N, M)

    def move_red():
        global escaped
        BR_r, BR_c = BR

        for c in range(BR_c, 0, -1):
            if new_maps[BR_r][c - 1] == '.':
                new_maps[BR_r][c - 1] = 'R'
                new_maps[BR_r][c] = '.'
            elif new_maps[BR_r][c - 1] == 'O':
                new_maps[BR_r][c] = '.'
                escaped = True
                break
            else:
                break

    def move_blue():
        global escaped, possible
        BB_r, BB_c = BB

        for c in range(BB_c, 0, -1):
            if new_maps[BB_r][c - 1] == '.':
                new_maps[BB_r][c - 1] = 'B'
                new_maps[BB_r][c] = '.'
            elif new_maps[BB_r][c - 1] == 'O':
                new_maps[BB_r][c] = '.'
                escaped = False
                possible = False
                break
            else:
                break

    if BR[0] == BB[0]:
        if BR[1] > BB[1]:
            move_blue()
            if possible:
                move_red()
        else:
            move_red()
            move_blue()
    else:
        move_red()
        move_blue()

    return new_maps


def move_right(maps, N, M):
    global escaped, possible
    possible = True
    new_maps = deepcopy(maps)

    BR, BB, HOLE = get_pos(maps, N, M)

    def move_red():
        global escaped
        BR_r, BR_c = BR

        for c in range(BR_c, M):
            if new_maps[BR_r][c + 1] == '.':
                new_maps[BR_r][c + 1] = 'R'
                new_maps[BR_r][c] = '.'
            elif new_maps[BR_r][c + 1] == 'O':
                new_maps[BR_r][c] = '.'
                escaped = True
                break
            else:
                break

    def move_blue():
        global escaped, possible
        BB_r, BB_c = BB

        for c in range(BB_c, M):
            if new_maps[BB_r][c + 1] == '.':
                new_maps[BB_r][c + 1] = 'B'
                new_maps[BB_r][c] = '.'
            elif new_maps[BB_r][c + 1] == 'O':
                new_maps[BB_r][c] = '.'
                escaped = False
                possible = False
                break
            else:
                break

    if BR[0] == BB[0]:
        if BR[1] < BB[1]:
            move_blue()
            if possible:
                move_red()
        else:
            move_red()
            move_blue()
    else:
        move_red()
        move_blue()

    return new_maps


def solution():
    global possible
    N, M = map(int, input().split())

    maps = list(list(input().rstrip()) for _ in range(N))

    q = deque([])

    q.append((maps, 0))

    while q:
        now, cnt = q.popleft()

        if cnt == 10:
            continue

        U = move_up(now, N, M)
        if now != U and possible:
            q.append((U, cnt + 1))

        D = move_down(now, N, M)
        if now != D and possible:
            q.append((D, cnt + 1))
        L = move_left(now, N, M)
        if now != L and possible:
            q.append((L, cnt + 1))
        R = move_right(now, N, M)
        if now != R and possible:
            q.append((R, cnt + 1))

        if escaped:
            print(cnt + 1)
            break

    if not escaped:
        print(-1)


solution()
