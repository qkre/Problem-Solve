import os
import sys


current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"input/{current_file}_input.txt", "r", encoding="utf-8-sig")

from collections import deque

result = []

T = int(input())

for case in range(1, T + 1):
    arr = list(deque(input()) for _ in range(5))

    s = ""

    while True:
        check = False

        for i in arr:
            if i:
                s += i.popleft()
                check = True
        
        if not check:
            break

    result.append(f"#{case} {s}")

for _ in result:
    print(_)


output = open(f"input/{current_file}_output.txt", "r").readlines()
output = [line.strip() for line in output]

print("------------------- 오답 ------------------ ( 이 아래로 출력이 없으면 정답)")

for r, o in zip(result, output):
    if r != o:
        print(f"정답 : {o},     오답 : {r}")
