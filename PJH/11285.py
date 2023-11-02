import os
import sys


current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"input/{current_file}_input.txt", "r", encoding="utf-8-sig")


result = []

T = int(input())

target = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200]

for case in range(1, T + 1):
    N = int(input())
    score = 0

    for _ in range(N):
        x, y = map(int, input().split())

        r = (x**2 + y**2) ** 0.5 * 2 * 3.14

        for i in range(10):
            if target[i] * 2 * 3.14 >= r:
                score += 10 - i
                break

    result.append(f"#{case} {score}")

for _ in result:
    print(_)


output = open(f"input/{current_file}_output.txt", "r").readlines()
output = [line.strip() for line in output]

print("------------------- 오답 ------------------ ( 이 아래로 출력이 없으면 정답)")

for r, o in zip(result, output):
    if r != o:
        print(f"정답 : {o},     오답 : {r}")
