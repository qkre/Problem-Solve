import os
import sys
from check_answer import check_answer

current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"../input/{current_file}.txt", "r", encoding="utf-8-sig")

from collections import deque, defaultdict
from pprint import pprint

result = []
for case in range(1, 10 + 1):
    ans = 0

    N = int(input())
    maps = list(list(map(int, list(input()))) for _ in range(100))

    start = (0, 0)
    end = (0, 0)

    for y in range(100):
        for x in range(100):
            if maps[y][x] == 2:
                start = (y, x)
            elif maps[y][x] == 3:
                end = (y, x)

    q = deque()
    q.append(start)

    while q:
        cy, cx = q.popleft()

        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ny, nx = cy + dy, cx + dx

            if 0 <= ny < 100 and 0 <= nx < 100:
                if maps[ny][nx] == 0:
                    maps[ny][nx] = 5
                    q.append((ny, nx))
                elif maps[ny][nx] == 3:
                    ans = 1
                    break


    result.append(f"#{case} {ans}")

for r in result:
    print(r)

check_answer(current_file, result)
