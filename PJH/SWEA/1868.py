import os
import sys
from check_answer import check_answer

current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"../input/{current_file}.txt", "r", encoding="utf-8-sig")

from collections import deque, defaultdict

T = int(input())
result = []


def count_bomb(y, x):
    count = 0
    for dy, dx in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
        ny, nx = y + dy, x + dx

        if 0 <= ny < N and 0 <= nx < N:
            if maps[ny][nx] == "*":
                count += 1

    return count


def click_tile(y, x):
    q = deque()
    q.append((y, x))
    while q:
        cy, cx = q.popleft()

        if not count_bomb(cy, cx):
            maps[cy][cx] = 0
            for dy, dx in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                ny, nx = cy + dy, cx + dx

                if 0 <= ny < N and 0 <= nx < N and maps[ny][nx] == ".":
                    if (ny, nx) not in q:
                        q.append((ny, nx))
        else:
            maps[cy][cx] = count_bomb(cy, cx)


def check():
    for y in range(N):
        for x in range(N):
            if maps[y][x] == ".":
                return True

    return False


for case in range(1, T + 1):
    ans = 0

    N = int(input())
    maps = list(list(input()) for _ in range(N))

    while check():
        clicked = False
        for y in range(N):
            for x in range(N):
                if maps[y][x] == "." and not count_bomb(y, x):
                    clicked = True
                    click_tile(y, x)
                    ans += 1


        if not clicked:
            break

    for y in range(N):
        for x in range(N):
            if maps[y][x] == ".":
                ans += 1


    result.append(f"#{case} {ans}")

for r in result:
    print(r)

check_answer(current_file, result)
