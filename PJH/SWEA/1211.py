import os
import sys
from check_answer import check_answer

current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"../input/{current_file}.txt", "r", encoding="utf-8-sig")

from collections import deque, defaultdict

result = []


def move(x):
    visited = [[False for _ in range(100)] for _ in range(100)]
    visited[0][x] = True
    moves = 0
    y = 0
    while y < 100:

        if y + 1 == 100:
            break

        if x-1 >= 0 and maps[y][x - 1] and not visited[y][x - 1]:
            visited[y][x - 1] = True
            x -= 1
            moves += 1
            continue
        elif x + 1 < 100 and maps[y][x + 1] and not visited[y][x + 1]:
            visited[y][x + 1] = True
            x += 1
            moves += 1
            continue
        else:
            visited[y+1][x] = True
            y += 1
            moves += 1

    return moves

for case in range(1, 10 + 1):
    ans = 0
    min_move = 1e9
    N = int(input())

    maps = list(list(map(int, input().split())) for _ in range(100))

    for i in range(100):
        if maps[0][i]:
            moves = move(i)
            if moves < min_move:
                min_move = moves
                ans = i

    result.append(f"#{case} {ans}")

for r in result:
    print(r)

check_answer(current_file, result)
