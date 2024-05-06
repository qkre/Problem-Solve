import os
import sys

current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"../../input/{current_file}_input.txt", "r", encoding="utf-8-sig")

from collections import deque

result = []
T = 10
for _ in range(1, T + 1):
    case = int(input())
    board = list(list(map(int, input().split())) for _ in range(100))
    visited = [[False for _ in range(100)] for _ in range(100)]
    ans = 0

    sx, sy = 0, 99
    for i in range(100):
        if board[sy][i] == 2:
            sx = i
            break

    q = deque()
    q.append((sx, sy))
    visited[sy][sx] = True

    while q:
        x, y = q.popleft()

        if y == 0:
            ans = x
            break

        if x - 1 >= 0 and board[y][x - 1] == 1 and not visited[y][x - 1]:
            visited[y][x - 1] = True
            q.append((x - 1, y))
        elif x + 1 < 100 and board[y][x + 1] == 1 and not visited[y][x + 1]:
            visited[y][x + 1] = True
            q.append((x + 1, y))
        else:
            visited[y - 1][x] = True
            q.append((x, y - 1))

    result.append(f"#{case} {ans}")
for _ in result:
    print(_)

output = open(f"../../input/{current_file}_output.txt", "r").readlines()
output = [line.strip() for line in output]

print("------------------- 오답 ------------------ ( 이 아래로 출력이 없으면 정답)")

for y, o in zip(result, output):
    if y != o:
        print(f"정답 : {o},     오답 : {y}")
