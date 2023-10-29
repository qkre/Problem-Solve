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

        print("R")
for _ in result:
    print(_)


output = open(f"input/{current_file}_output.txt", "r").readlines()
output = [line.strip() for line in output]

print("------------------- 오답 ------------------ ( 이 아래로 출력이 없으면 정답)")

for r, o in zip(result, output):
    if r != o:
        print(f"정답 : {o},     오답 : {r}")
