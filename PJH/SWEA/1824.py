import os
import sys
from check_answer import check_answer

current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"../input/{current_file}.txt", "r", encoding="utf-8-sig")

from collections import deque, defaultdict

T = int(input())
result = []

def move(r, c, d):
    global R, C
    if d == "L":
        return r, (c - 1) % C
    if d == "R":
        return r, (c + 1) % C
    if d == "U":
        return (r - 1) % R, c
    if d == "D":
        return (r + 1) % R, c

for case in range(1, T + 1):
    ans = "NO"
    R, C = map(int, input().split())
    maps = list(list(input()) for _ in range(R))
    visited = defaultdict(bool)

    q = deque([(0, 0, 0, "R")])

    while q:
        r, c, m, d = q.popleft()

        if maps[r][c] == "<":
            d = "L"
        elif maps[r][c] == ">":
            d = "R"
        elif maps[r][c] == "^":
            d = "U"
        elif maps[r][c] == 'v':
            d = "D"
        elif maps[r][c] == '_':
            d = "R" if m == 0 else "L"
        elif maps[r][c] == '|':
            d = "D" if m == 0 else "U"
        elif maps[r][c].isdigit():
            m = int(maps[r][c])
        elif maps[r][c] == "+":
            m = (m + 1) % 16
        elif maps[r][c] == '-':
            m = (m - 1) % 16
        elif maps[r][c] == "?":
            for nd in "LRUD":
                nr, nc = move(r, c, nd)
                if not visited[(nr, nc, m, nd)]:
                    visited[(nr, nc, m, nd)] = True
                    q.append((nr, nc, m, nd))
        elif maps[r][c] == "@":
            ans = "YES"
            break

        r, c = move(r, c, d)
        if not visited[(r, c, m, d)]:
            visited[(r, c, m, d)] = True
            q.append((r, c, m, d))


    result.append(f"#{case} {ans}")

for r in result:
    print(r)

check_answer(current_file, result)
