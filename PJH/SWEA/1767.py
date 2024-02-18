import sys

sys.stdin = open("input/1767_input.txt", "r")

T = int(input())


def check(direction, y, x):
    global N

    if direction == 0:
        for i in range(x):
            if maxinos[y][i] != 0:
                return False

    elif direction == 1:
        for i in range(x + 1, N):
            if maxinos[y][i] != 0:
                return False

    elif direction == 2:
        for i in range(y):
            if maxinos[i][x] != 0:
                return False

    elif direction == 3:
        for i in range(y + 1, N):
            if maxinos[i][x] != 0:
                return False

    return True


def draw(direction, y, x):
    global N

    if direction == 0:
        for i in range(x):
            maxinos[y][i] = 2

    elif direction == 1:
        for i in range(x + 1, N):
            maxinos[y][i] = 2

    elif direction == 2:
        for i in range(y):
            maxinos[i][x] = 2

    elif direction == 3:
        for i in range(y + 1, N):
            maxinos[i][x] = 2


def erase(direction, y, x):
    global N

    if direction == 0:
        for i in range(x):
            maxinos[y][i] = 0

    elif direction == 1:
        for i in range(x + 1, N):
            maxinos[y][i] = 0

    elif direction == 2:
        for i in range(y):
            maxinos[i][x] = 0

    elif direction == 3:
        for i in range(y + 1, N):
            maxinos[i][x] = 0


def dfs(y, x, cnt, wires):
    global N, res, cores

    if x == N - 1 and y == N - 1:
        if cores == cnt:
            cores = cnt
            res = min(res, wires)
        elif cores < cnt:
            cores = cnt
            res = wires

        return

    if y == 0:
        y += 1
    if x == 0:
        x += 1

    if x == N - 1:
        x = 1
        y += 1

    if maxinos[y][x] == 1:
        if check(0, y, x):
            draw(0, y, x)
            dfs(y, x + 1, cnt + 1, wires + x)
            erase(0, y, x)
        if check(1, y, x):
            draw(1, y, x)
            dfs(y, x + 1, cnt + 1, wires + (N - x - 1))
            erase(1, y, x)
        if check(2, y, x):
            draw(2, y, x)
            dfs(y, x + 1, cnt + 1, wires + y)
            erase(2, y, x)
        if check(3, y, x):
            draw(3, y, x)
            dfs(y, x + 1, cnt + 1, wires + (N - y - 1))
            erase(3, y, x)

        dfs(y, x + 1, cnt, wires)
    else:
        dfs(y, x + 1, cnt, wires)


for case in range(1, T + 1):
    N = int(input())
    maxinos = list(list(map(int, input().split())) for _ in range(N))
    res = N * N
    cores = 0
    dfs(1, 1, 0, 0)
    print(f"#{case} {res}")
