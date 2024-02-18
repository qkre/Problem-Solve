import os
import sys


current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"input/{current_file}_input.txt", "r", encoding="utf-8-sig")


result = []

T = int(input())

import copy

for case in range(1, T + 1):
    arr = list(input())
    index = 0
    original = copy.deepcopy(arr)

    for i in arr:
        if original.count(i) > 1:
            original.remove(i)
            original.remove(i)

    original.sort()

    if len(original) > 0:
        result.append(f"#{case} {''.join(original)}")
    else:
        result.append(f"#{case} Good")

for _ in result:
    print(_)


output = open(f"input/{current_file}_output.txt", "r").readlines()
output = [line.strip() for line in output]

print("------------------- 오답 ------------------ ( 이 아래로 출력이 없으면 정답)")

for r, o in zip(result, output):
    if r != o:
        print(f"정답 : {o},     오답 : {r}")
