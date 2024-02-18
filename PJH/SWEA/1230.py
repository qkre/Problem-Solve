import os
import sys


current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"input/{current_file}_input.txt", "r")


result = []

T = 10

for case in range(1, T + 1):
    N = int(input())

    original_code = list(input().split(" "))

    C = int(input())

    commands = list(input().split(" "))

    for i in range(len(commands)):
        if commands[i] == "I":
            x = int(commands[i + 1])
            y = int(commands[i + 2])
            for j in range(y):
                original_code.insert(x + j, commands[j + i + 3])

        elif commands[i] == "D":
            x = int(commands[i + 1])
            y = int(commands[i + 2])
            original_code = original_code[:x] + original_code[x + y + 1 :]

        elif commands[i] == "A":
            y = int(commands[i + 1])
            for j in range(i + 2, i + y):
                original_code.append(commands[j])

    result.append(f"#{case} {' '.join(original_code[:10])}")

for _ in result:
    print(_)


output = open(f"input/{current_file}_output.txt", "r").readlines()
output = [line.strip() for line in output]

print("------------------- 오답 ------------------ ( 이 아래로 출력이 없으면 정답)")

for r, o in zip(result, output):
    if r != o:
        print(f"정답 : {o},     오답 : {r}")
