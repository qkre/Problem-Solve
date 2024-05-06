import os
import sys

current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"../../input/{current_file}_input.txt", "r", encoding="utf-8-sig")

from collections import deque
sys.setrecursionlimit(10**5)
result = []
T = int(input())


def decode(cmd, m, d):
    if cmd == "<":
        return m, "L"

    if cmd == ">":
        return m, "R"

    if cmd == "^":
        return m, "U"

    if cmd == "v":
        return m, "D"

    if cmd == "_":
        if m == 0:
            return m, "R"
        else:
            return m, "L"
    if cmd == "|":
        if m == 0:
            return m, "D"
        else:
            return m, "U"
    if cmd.isdigit():
        return int(cmd), d
    if cmd == "+":
        return (m + 1) % 16, d
    if cmd == "-":
        return (m - 1) % 16, d

    return m, d


def move(r, c, d):
    if d == "L":
        return r, c - 1 if c - 1 >= 0 else C - 1
    if d == "R":
        return r, c + 1 if c + 1 < C else 0
    if d == "U":
        return r - 1 if r - 1 >= 0 else R - 1, c
    if d == "D":
        return r + 1 if r + 1 < R else 0, c

def dfs(r, c, m, d, path):
    global ans, pos

    if (r, c) == pos:
        ans = "YES"
        return

    if board[r][c] != "?":
        m, d = decode(board[r][c], m, d)
        r, c = move(r, c, d)

        if (r, c, m, d) not in path:
            path.append((r, c, m, d))
            dfs(r, c, m, d, path)
            path.pop()
    else:
        for nd in "LRUD":
            nr, nc = move(r, c, nd)

            if (nr, nc, m, nd) not in path:
                path.append((nr, nc, m, nd))
                dfs(nr, nc, m, nd, path)


for case in range(1, T + 1):
    ans = "NO"
    R, C = map(int, input().split())
    board = list(list(input()) for _ in range(R))

    pos = (-1, -1)
    for i in range(R):
        for j in range(C):
            if board[i][j] == '@':
                pos = (i, j)

    if pos != (-1, -1):
        dfs(0, 0, 0, "R", [])

    result.append(f"#{case} {ans}")
for _ in result:
    print(_)

output = open(f"../../input/{current_file}_output.txt", "r").readlines()
output = [line.strip() for line in output]

print("------------------- 오답 ------------------ ( 이 아래로 출력이 없으면 정답)")

for y, o in zip(result, output):
    if y != o:
        print(f"정답 : {o},     오답 : {y}")
