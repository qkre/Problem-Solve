import os
import sys

current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"../../input/{current_file}_input.txt", "r", encoding="utf-8-sig")

from collections import deque

result = []

for _ in range(10):
    case = int(input())
    ans = 0
    board = list(list(map(int, list(input()))) for _ in range(16))
    visited = [[False for _ in range(16)] for _ in range(16)]
    sy, sx, ey, ex = 0, 0, 0, 0

    for i in range(16):
        for j in range(16):
            if board[i][j] == 2:
                sy, sx = i, j
            if board[i][j] == 3:
                ey, ex = i, j

    q = deque()
    q.append((sy, sx))
    visited[sy][sx] = True

    while q:
        y, x = q.popleft()

        if y == ey and x == ex:
            ans = 1
            break

        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ny, nx = y + dy, x + dx

            if 0 <= ny < 16 and 0 <= nx < 16:
                if board[ny][nx] == 0:
                    board[ny][nx] = 2
                    q.append((ny, nx))
                elif board[ny][nx] == 3:
                    ans = 1
                    break


    result.append(f"#{case} {ans}")
for _ in result:
    print(_)

output = open(f"../../input/{current_file}_output.txt", "r").readlines()
output = [line.strip() for line in output]

print("------------------- 오답 ------------------ ( 이 아래로 출력이 없으면 정답)")

for y, o in zip(result, output):
    if y != o:
        print(f"정답 : {o},     오답 : {y}")
