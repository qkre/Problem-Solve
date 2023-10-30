import os
import sys


current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"input/{current_file}_input.txt", "r")


result = []

T = int(input())

for case in range(1, T + 1):
    N = int(input())
    now = 0
    speed = 0
    for _ in range(N):
        command = list(map(int, input().split()))

        if command[0] == 1:
            speed += command[1]
        elif command[0] == 2:
            speed -= command[1] if speed - command[1] >= 0 else 0

        now += speed

    result.append(f"#{case} {now}")


for _ in result:
    print(_)


output = open(f"input/{current_file}_output.txt", "r").readlines()
output = [line.strip() for line in output]

print("------------------- 오답 ------------------ ( 이 아래로 출력이 없으면 정답)")

for r, o in zip(result, output):
    if r != o:
        print(f"정답 : {o},     오답 : {r}")
