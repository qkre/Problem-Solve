import os
import sys


current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"input/{current_file}_input.txt", "r", encoding="utf-8-sig")


result = []

T = int(input())

import copy


for case in range(1, T + 1):
    N = int(input())
    arr = []
    while len(arr) != N:
        temp = list(map(int, input().split()))
        for i in temp:
            arr.append(i)

    checked = []

    for i in range(10):
        if i not in arr:
            checked.append(False)
        else:
            checked.append(True)

    if False in checked:
        result.append(f"#{case} {checked.index(False)}")
    else:
        find = False
        for i in range(2, N):
            perms = []

            for j in range(N - 1):
                perms.append(int("".join(map(str, arr[j : j + i]))))
            perms.sort()
            for j in range(10 ** (i - 1), perms[-1]):
                if j not in perms:
                    result.append(f"#{case} {j}")
                    find = True
                    break

            if find:
                break


for _ in result:
    print(_)


output = open(f"input/{current_file}_output.txt", "r").readlines()
output = [line.strip() for line in output]

print("------------------- 오답 ------------------ ( 이 아래로 출력이 없으면 정답)")

for r, o in zip(result, output):
    if r != o:
        print(f"정답 : {o},     오답 : {r}")
