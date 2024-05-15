import os
import sys

current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"../../input/{current_file}_input.txt", "r", encoding="utf-8-sig")

from collections import deque, defaultdict

result = []
T = int(input())


def row_check(x, y):
    for i in range(5):
        if x + i >= N or maps[y][x + i] != "o":
            return False
    return True


def col_check(x, y):
    for i in range(5):
        if y + i >= N or maps[y + i][x] != 'o':
            return False
    return True


def dia_check(x, y):
    for i in range(5):
        if y + i >= N or x + i >= N or maps[y + i][x + i] != 'o':
            return False
    return True


def rdia_check(x, y):
    for i in range(5):
        if y + i >= N or x - i < 0 or maps[y + i][x - i] != 'o':
            return False
    return True


for case in range(1, T + 1):
    ans = False
    N = int(input())
    maps = list(list(input()) for _ in range(N))

    for y in range(N):
        for x in range(N):
            ans = row_check(x, y) or col_check(x, y) or dia_check(x, y) or rdia_check(x, y)
            if ans:
                break
        if ans:
            break

    ans = "YES" if ans else "NO"

    result.append(f"#{case} {ans}")
for _ in result:
    print(_)

output = open(f"../../input/{current_file}_output.txt", "r").readlines()
output = [line.strip() for line in output]

print("------------------- 오답 ------------------ ( 이 아래로 출력이 없으면 정답)")

for y, o in zip(result, output):
    if y != o:
        print(f"정답 : {o},     오답 : {y}")
