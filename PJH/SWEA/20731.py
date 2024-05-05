import os
import sys
from math import gcd

current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"../../input/{current_file}_input.txt", "r", encoding="utf-8-sig")

import math

result = []
T = int(input())
for case in range(1, T+1):

    N = int(input())
    board = list(list(input()) for _ in range(N))
    ans = "YES"
    for r in range(1, N+1):
        for c in range(1, N+1):
            K = max(r, c)

            check = False
            for k in range(K+1):
                d = gcd(r+k, c+k)
                if d != 1:
                    check = True
                    break
            if check and board[r-1][c-1] == '1':
                continue
            elif not check and board[r-1][c-1] == '?':
                continue
            else:
                ans = "NO"

    result.append(f"#{case} {ans}")

for _ in result:
    print(_)


output = open(f"../../input/{current_file}_output.txt", "r").readlines()
output = [line.strip() for line in output]

print("------------------- 오답 ------------------ ( 이 아래로 출력이 없으면 정답)")

for r, o in zip(result, output):
    if r != o:
        print(f"정답 : {o},     오답 : {r}")
