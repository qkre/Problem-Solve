from sys import stdin
from collections import deque
from copy import deepcopy

input = stdin.readline


def move_up(maps, N):
    new_maps = deepcopy(maps)

    no_blanks = [[0 for _ in range(N)] for _ in range(N)]
    # 공백 없애기.
    for c in range(N):
        q = deque()
        for r in range(N):
            if new_maps[r][c] != 0:
                q.append(new_maps[r][c])

        idx = 0
        while q:
            no_blanks[idx][c] = q.popleft()
            idx += 1

    new_maps = no_blanks


    for c in range(N):
        for r in range(N - 1):
            if new_maps[r][c] == new_maps[r + 1][c] and new_maps[r][c] != 0:
                new_maps[r][c] = new_maps[r][c] * 2
                for k in range(r + 1, N):
                    if k + 1 < N:
                        new_maps[k][c] = new_maps[k + 1][c]
                    else:
                        new_maps[k][c] = 0

    no_blanks = [[0 for _ in range(N)] for _ in range(N)]
    # 공백 없애기.
    for c in range(N):
        q = deque()
        for r in range(N):
            if new_maps[r][c] != 0:
                q.append(new_maps[r][c])

        idx = 0
        while q:
            no_blanks[idx][c] = q.popleft()
            idx += 1


    return no_blanks


def move_down(maps, N):
    new_maps = deepcopy(maps)

    no_blanks = [[0 for _ in range(N)] for _ in range(N)]
    for c in range(N):
        stack = []
        for r in range(N):
            if new_maps[r][c] != 0:
                stack.append(new_maps[r][c])

        idx = N-1
        while stack:
            no_blanks[idx][c] = stack.pop()
            idx -= 1

    new_maps = no_blanks

    for c in range(N):
        for r in range(N - 1, 0, -1):
            if new_maps[r][c] == new_maps[r - 1][c] and new_maps[r][c] != 0:
                new_maps[r][c] = new_maps[r][c] * 2
                for k in range(r - 1, -1, -1):
                    if k - 1 >= 0:
                        new_maps[k][c] = new_maps[k - 1][c]
                    else:
                        new_maps[k][c] = 0

    no_blanks = [[0 for _ in range(N)] for _ in range(N)]
    for c in range(N):
        stack = []
        for r in range(N):
            if new_maps[r][c] != 0:
                stack.append(new_maps[r][c])

        idx = N-1
        while stack:
            no_blanks[idx][c] = stack.pop()
            idx -= 1

    return no_blanks


def move_left(maps, N):
    new_maps = deepcopy(maps)

    no_blanks = [[0 for _ in range(N)] for _ in range(N)]
    for r in range(N):
        q = deque()
        for c in range(N):
            if new_maps[r][c] != 0:
                q.append(new_maps[r][c])

        idx = 0
        while q:
            no_blanks[r][idx] = q.popleft()
            idx += 1

    new_maps = no_blanks

    for r in range(N):
        for c in range(N - 1):
            if new_maps[r][c] == new_maps[r][c + 1] and new_maps[r][c] != 0:
                new_maps[r][c] = new_maps[r][c] * 2
                for k in range(c + 1, N):
                    if k + 1 < N:
                        new_maps[r][k] = new_maps[r][k + 1]
                    else:
                        new_maps[r][k] = 0

    no_blanks = [[0 for _ in range(N)] for _ in range(N)]
    for r in range(N):
        q = deque()
        for c in range(N):
            if new_maps[r][c] != 0:
                q.append(new_maps[r][c])

        idx = 0
        while q:
            no_blanks[r][idx] = q.popleft()
            idx += 1

    return no_blanks


def move_right(maps, N):
    new_maps = deepcopy(maps)

    no_blanks = [[0 for _ in range(N)] for _ in range(N)]
    for r in range(N):
        stack = []
        for c in range(N):
            if new_maps[r][c] != 0:
                stack.append(new_maps[r][c])

        idx = N - 1
        while stack:
            no_blanks[r][idx] = stack.pop()
            idx -= 1

    new_maps = no_blanks

    for r in range(N):
        for c in range(N - 1, 0, -1):
            if new_maps[r][c] == new_maps[r][c - 1] and new_maps[r][c] != 0:
                new_maps[r][c] = new_maps[r][c] * 2
                for k in range(c - 1, -1, -1):
                    if k - 1 >= 0:
                        new_maps[r][k] = new_maps[r][k - 1]
                    else:
                        new_maps[r][k] = 0

    no_blanks = [[0 for _ in range(N)] for _ in range(N)]
    for r in range(N):
        stack = []
        for c in range(N):
            if new_maps[r][c] != 0:
                stack.append(new_maps[r][c])

        idx = N - 1
        while stack:
            no_blanks[r][idx] = stack.pop()
            idx -= 1

    return no_blanks


def print_maps(maps):
    print("##########")
    for _ in maps:
        print(*_)
    print("##########")


def solution():
    N = int(input())

    maps = list(list(map(int, input().split())) for _ in range(N))

    q = deque([(maps, 0)])

    answer = 0
    for _ in maps:
        answer = max(answer, max(_))

    while q:
        now, cnt = q.popleft()

        for _ in now:
            answer = max(answer, max(_))

        if cnt == 5:
            continue

        U = move_up(now, N)
        if U != now:
            q.append((U, cnt + 1))
        D = move_down(now, N)
        if D != now:
            q.append((D, cnt + 1))
        L = move_left(now, N)
        if L != now:
            q.append((L, cnt + 1))
        R = move_right(now, N)
        if R != now:
            q.append((R, cnt + 1))

    print(answer)

solution()
