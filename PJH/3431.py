import os
import sys


current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"input/{current_file}_input.txt", "r", encoding="utf-8-sig")


result = []

T = int(input())

for case in range(1, T + 1):
    L, U, X = map(int, input().split())

    if X > U:
        result.append(f"#{case} -1")
    elif X >= L:
        result.append(f"#{case} 0")
    else:
        result.append(f"#{case} {L-X}")


for _ in result:
    print(_)


output = open(f"input/{current_file}_output.txt", "r").readlines()
output = [line.strip() for line in output]

print("------------------- 오답 ------------------ ( 이 아래로 출력이 없으면 정답)")

for r, o in zip(result, output):
    if r != o:
        print(f"정답 : {o},     오답 : {r}")
