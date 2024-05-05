import os
import sys

current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"../../input/{current_file}_input.txt", "r", encoding="utf-8-sig")

from math import gcd

result = []
T = int(input())
for case in range(1, T + 1):

    N = int(input())
    board = list(list(input()) for _ in range(N))
    ans = False

    for K in range(N+1):
        ans = True
        for i in range(N):
            for j in range(N):
                if gcd(i + 1 + K, j + 1 + K) == 1:
                    if board[i][j] != '1':
                        ans = False
                        break
                else:
                    if board[i][j] != '?':
                        ans = False
                        break
            if not ans:
                break
        if ans:
            break

    result.append(f"#{case} {'YES' if ans else 'NO'}")

for _ in result:
    print(_)

output = open(f"../../input/{current_file}_output.txt", "r").readlines()
output = [line.strip() for line in output]

print("------------------- 오답 ------------------ ( 이 아래로 출력이 없으면 정답)")

for r, o in zip(result, output):
    if r != o:
        print(f"정답 : {o},     오답 : {r}")
