import os
import sys

current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"../../input/{current_file}_input.txt", "r", encoding="utf-8-sig")

from collections import deque, defaultdict

result = []
T = int(input())


def put(x, y, c):
    global maps
    maps[y][x] = c

    row_check(x, y, c)
    col_check(x, y, c)
    dia_check(x, y, c)
    rdia_check(x, y, c)


def row_check(x, y, c):
    is_closed = False
    for i in range(x):
        if maps[y][i] == c:
            is_closed = True

        if maps[y][i] != "." and maps[y][i] != c and is_closed:
            maps[y][i] = c

    is_closed = False

    for i in range(N - 1, x, -1):
        if maps[y][i] == c:
            is_closed = True

        if maps[y][i] != "." and maps[y][i] != c and is_closed:
            maps[y][i] = c


def col_check(x, y, c):
    is_closed = False
    for i in range(y):
        if maps[i][x] == c:
            is_closed = True

        if maps[i][x] != "." and maps[i][x] != c and is_closed:
            maps[i][x] = c

    is_closed = False
    for i in range(N - 1, y, -1):
        if maps[i][x] == c:
            is_closed = True

        if maps[i][x] != "." and maps[i][x] != c and is_closed:
            maps[i][x] = c


def dia_check(x, y, c):
    is_closed = False

    for i in range(min(x, y), 0, -1):
        if maps[y - i][x - i] == c:
            is_closed = True

        if maps[y - i][x - i] != "." and maps[y - i][x - i] != c and is_closed:
            maps[y - i][x - i] = c

    is_closed = False
    for i in range(N - max(x, y) - 1, 0, -1):
        if maps[y + i][x + i] == c:
            is_closed = True

        if maps[y + i][x + i] != "." and maps[y + i][x + i] != c and is_closed:
            maps[y + i][x + i] = c


def rdia_check(x, y, c):
    is_closed = False

    for i in range(max(x, y), 0, -1):
        if y - i < 0 or x + i >= N:
            break

        if maps[y - i][x + i] == c:
            is_closed = True

        if maps[y - i][x + i] != "." and maps[y - i][x + i] != c and is_closed:
            maps[y - i][x + i] = c

    is_closed = False

    for i in range(max(x, y), 0, -1):
        if y + i >= N or x - i < 0:
            break

        if maps[y + i][x - i] == c:
            is_closed = True
        if maps[y + i][x - i] != "." and maps[y + i][x - i] != c and is_closed:
            maps[y + i][x - i] = c


for case in range(1, T + 1):

    N, M = map(int, input().split())
    maps = list(list("." * N) for _ in range(N))

    maps[N // 2][N // 2] = maps[N // 2 - 1][N // 2 - 1] = "W"
    maps[N // 2 - 1][N // 2] = maps[N // 2][N // 2 - 1] = "B"

    for _ in range(M):
        x, y, c = map(int, input().split())
        put(x - 1, y - 1, "B" if c == 1 else "W")

    black = 0
    white = 0

    for i in range(N):
        for j in range(N):
            if maps[i][j] == 'B':
                black += 1
            elif maps[i][j] == 'W':
                white += 1

    result.append(f"#{case} {black} {white}")
for _ in result:
    print(_)

output = open(f"../../input/{current_file}_output.txt", "r").readlines()
output = [line.strip() for line in output]

print("------------------- 오답 ------------------ ( 이 아래로 출력이 없으면 정답)")

for y, o in zip(result, output):
    if y != o:
        print(f"정답 : {o},     오답 : {y}")
