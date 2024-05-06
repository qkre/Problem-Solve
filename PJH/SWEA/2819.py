import os
import sys

current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"../../input/{current_file}_input.txt", "r", encoding="utf-8-sig")

result = []
T = int(input())

def dfs(depth, x, y, number):
    if depth == 7:
        ans.add(number)
        return


    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy

        if 0 <= nx < 4 and 0 <= ny < 4:
            dfs(depth + 1, nx, ny, number + board[ny][nx])


for case in range(1, T + 1):
    board = [list(input().split()) for _ in range(4)]

    ans = set()
    visited = []

    for i in range(4):
        for j in range(4):
            dfs(1, j, i, board[i][j])


    result.append(f"#{case} {len(ans)}")
for _ in result:
    print(_)

output = open(f"../../input/{current_file}_output.txt", "r").readlines()
output = [line.strip() for line in output]

print("------------------- 오답 ------------------ ( 이 아래로 출력이 없으면 정답)")

for r, o in zip(result, output):
    if r != o:
        print(f"정답 : {o},     오답 : {r}")
