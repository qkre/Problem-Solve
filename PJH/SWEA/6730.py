import os
import sys


current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"input/{current_file}_input.txt", "r", encoding="utf-8-sig")


result = []

T = int(input())

for case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    max_up = 0
    max_down = 0

    for i in range(N - 1):
        if arr[i] < arr[i + 1]:
            max_up = max(arr[i + 1] - arr[i], max_up)
        else:
            max_down = max(arr[i] - arr[i + 1], max_down)

    result.append(f"#{case} {max_up} {max_down}")

for _ in result:
    print(_)


output = open(f"input/{current_file}_output.txt", "r").readlines()
output = [line.strip() for line in output]

print("------------------- 오답 ------------------ ( 이 아래로 출력이 없으면 정답)")

for r, o in zip(result, output):
    if r != o:
        print(f"정답 : {o},     오답 : {r}")
