import os
import sys


current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"input/{current_file}_input.txt", "r")


T = int(input())
result = []
for case in range(1, T + 1):
    string = list(input())

    checked = True

    for i in range(1, len(string) + 1):
        if string[:i] == string[i : i * 2]:
            result.append(f"#{case} {i}")
            break


for _ in result:
    print(_)


output = open(f"input/{current_file}_output.txt", "r").readlines()
output = [line.strip() for line in output]

print("------------------- 오답 ------------------ ( 이 아래로 출력이 없으면 정답)")

for r, o in zip(result, output):
    if r != o:
        print(f"정답 : {o},     오답 : {r}")