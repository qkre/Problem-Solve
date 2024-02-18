import os
import sys


current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"input/{current_file}_input.txt", "r", encoding="utf-8-sig")


result = []

T = int(input())

for case in range(1, T + 1):
    arr = list(map(int, input().split()))
    if arr.count(arr[0]) == 3:
        result.append(f"#{case} {arr[0]}")
    else:
        if arr.count(arr[0]) != 2:
            result.append(f"#{case} {arr[0]}")
        elif arr.count(arr[1]) != 2:
            result.append(f"#{case} {arr[1]}")
        else:
            result.append(f"#{case} {arr[2]}")


for _ in result:
    print(_)


output = open(f"input/{current_file}_output.txt", "r").readlines()
output = [line.strip() for line in output]

print("------------------- 오답 ------------------ ( 이 아래로 출력이 없으면 정답)")

for r, o in zip(result, output):
    if r != o:
        print(f"정답 : {o},     오답 : {r}")
