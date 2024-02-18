import os
import sys


current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"input/{current_file}_input.txt", "r", encoding="utf-8-sig")


result = []

T = int(input())

for case in range(1, T + 1):
    A, B = map(int, input().split())
    cnt = 0
    for N in range(A, B + 1):
        str_N = list(str(N))
        if (N**0.5) % 1 != 0:
            continue
        str_sqrt_N = list(str(int(N**0.5)))

        if str_N == list(reversed(str_N)) and str_sqrt_N == list(reversed(str_sqrt_N)):
            cnt += 1

    result.append(f"#{case} {cnt}")


for _ in result:
    print(_)


output = open(f"input/{current_file}_output.txt", "r").readlines()
output = [line.strip() for line in output]

print("------------------- 오답 ------------------ ( 이 아래로 출력이 없으면 정답)")

for r, o in zip(result, output):
    if r != o:
        print(f"정답 : {o},     오답 : {r}")
