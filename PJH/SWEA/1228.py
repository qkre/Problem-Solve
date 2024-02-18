import os
import sys


current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"input/{current_file}_input.txt", "r")


result = []

T = 10

for case in range(1, T + 1):
    N = int(input())

    original_code = input().split(" ")
    original_code = original_code[:-1]

    C = int(input())
    cmds = list(input().split("I"))
    cmds = cmds[1:]

    for cmd in cmds:
        codes = cmd[1:-1].split(" ")
        x = int(codes[0])
        y = int(codes[1])
        s = codes[2:]

        for i in range(y):
            original_code.insert(x + i, s[i])

    result.append(f"#{case} {' '.join(original_code[:10])}")

for _ in result:
    print(_)


output = open(f"input/{current_file}_output.txt", "r").readlines()
output = [line.strip() for line in output]

print("------------------- 오답 ------------------ ( 이 아래로 출력이 없으면 정답)")

for r, o in zip(result, output):
    if r != o:
        print(f"정답 : {o},     오답 : {r}")
