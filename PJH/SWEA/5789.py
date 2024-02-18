import os
import sys


current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"input/{current_file}_input.txt", "r", encoding="utf-8-sig")


result = []

T = int(input())

for case in range(1, T + 1):
    N, Q = map(int, input().split())
    arr = [0] * N

    for i in range(1, Q + 1):
        S, E = map(int, input().split())

        arr[S - 1 : E] = [i] * (E - S + 1)

    result.append(f"#{case} {' '.join(list(map(str, arr)))}")

for _ in result:
    print(_)


output = open(f"input/{current_file}_output.txt", "r").readlines()
output = [line.strip() for line in output]

print("------------------- 오답 ------------------ ( 이 아래로 출력이 없으면 정답)")

for r, o in zip(result, output):
    if r != o:
        print(f"정답 : {o},     오답 : {r}")
