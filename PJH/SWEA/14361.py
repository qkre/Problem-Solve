import os
import sys


current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"input/{current_file}_input.txt", "r", encoding="utf-8-sig")


result = []

T = int(input())

for case in range(1, T + 1):
    N = int(input())
    N_string = list(str(N))
    KN = N

    if len(N_string) == 1:
        result.append(f"#{case} impossible")
        continue

    for i in range(2, 10000000):
        if len(list(str(KN * i))) != len(N_string):
            result.append(f"#{case} impossible")
            break

        if list(sorted(str(KN * i))) == list(sorted(N_string)):
            result.append(f"#{case} possible")
            break

for _ in result:
    print(_)


output = open(f"input/{current_file}_output.txt", "r").readlines()
output = [line.strip() for line in output]

print("------------------- 오답 ------------------ ( 이 아래로 출력이 없으면 정답)")

for r, o in zip(result, output):
    if r != o:
        print(f"정답 : {o},     오답 : {r}")
