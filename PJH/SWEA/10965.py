import os
import sys


current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"input/{current_file}_input.txt", "r", encoding="utf-8-sig")

import math

result = []

T = int(input())


def is_prime():
    N = 10000001

    seive = [True] * N

    m = int(N**0.5)

    for i in range(2, m + 1):
        if seive[i] == True:
            for j in range(i + i, m, i):
                seive[j] = False

    return [i for i in range(2, N) if seive[i]]


prime_list = is_prime()

for case in range(1, T + 1):
    A = int(input())

    if A**0.5 % 1 == 0:
        result.append(f"#{case} 1")
        continue

    elif A in prime_list:
        result.append(f"#{case} {A}")
        continue
    else:
        for i in range(2, A + 1):
            if (A * i) ** 0.5 % 1 == 0:
                result.append(f"#{case} {i}")
                break

for _ in result:
    print(_)


output = open(f"input/{current_file}_output.txt", "r").readlines()
output = [line.strip() for line in output]

print("------------------- 오답 ------------------ ( 이 아래로 출력이 없으면 정답)")

for r, o in zip(result, output):
    if r != o:
        print(f"정답 : {o},     오답 : {r}")
