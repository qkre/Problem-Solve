import os
import sys


current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"input/{current_file}_input.txt", "r", encoding="utf-8-sig")


result = []

T = int(input())

for case in range(1, T + 1):
    D, H, M = map(int, input().split())

    if D < 11 or (D == 11 and H < 11) or (D == 11 and H == 11 and M < 11):
        result.append(f"#{case} -1")
        continue

    D -= 11
    H -= 11
    M -= 11

    ans = D * 60 * 24 + H * 60 + M
    result.append(f"#{case} {ans}")


for _ in result:
    print(_)


output = open(f"input/{current_file}_output.txt", "r").readlines()
output = [line.strip() for line in output]

print("------------------- 오답 ------------------ ( 이 아래로 출력이 없으면 정답)")

for r, o in zip(result, output):
    if r != o:
        print(f"정답 : {o},     오답 : {r}")
