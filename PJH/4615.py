import os
import sys


current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"input/{current_file}_input.txt", "r")


result = []

T = int(input())

for case in range(1, T + 1):
    N, M = map(int, input().split())

    board = list([0] * N for _ in range(N))
    board[N // 2 - 1][N // 2 - 1] = 1
    board[N // 2 - 1][N // 2] = 2
    board[N // 2][N // 2 - 1] = 2
    board[N // 2][N // 2] = 1

    for _ in range(M):
        x, y, c = map(int, input().split())

        board[y - 1][x - 1] = c

        if c in board[y - 1]:
            first_index = board[y - 1].index(c)
            last_index = N - list(reversed(board[y - 1])).index(c)

            if not 0 in board[y - 1][first_index:last_index]:
                board[y - 1][first_index:last_index] = [c] * (last_index - first_index)

        row = [board[i][x - 1] for i in range(N)]

        if c in row:
            first_index = row.index(c)
            last_index = N - list(reversed(row)).index(c)

            if not 0 in row[first_index:last_index]:
                for i in range(first_index, last_index):
                    board[i][x - 1] = c

        rd = []
        ld = []

        sx, sy = x, y

        while sy > 0:
            sy -= 1
            sx -= 1

            if sy == 0 or sx == 0:
                break

        for i in range(N - sx):
            if sy + i == N:
                break
            rd.append(board[sy + i][sx + i])

        for i in range(sx + 1):
            if sy + i == N or sx - i < 0:
                break
            ld.append(board[sy + i][sx - i])

        if rd.count(c) >= 2:
            first_index = rd.index(c)
            last_index = len(rd) - list(reversed(rd)).index(c)

            for i in range(first_index, last_index):
                board[sy + i][sx + i] = c

        if ld.count(c) >= 2:
            first_index = ld.index(c)
            last_index = len(ld) - list(reversed(ld)).index(c)

            for i in range(first_index, last_index):
                board[sy + i][sx - i] = c

    white = 0
    black = 0

    for _ in board:
        white += _.count(1)
        black += _.count(2)

    result.append(f"#{case} {white} {black}")

for _ in result:
    print(_)


output = open(f"input/{current_file}_output.txt", "r").readlines()
output = [line.strip() for line in output]

print("------------------- 오답 ------------------ ( 이 아래로 출력이 없으면 정답)")

for r, o in zip(result, output):
    if r != o:
        print(f"정답 : {o},     오답 : {r}")
