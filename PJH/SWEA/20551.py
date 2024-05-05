import os
import sys
from test import check_answer

current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"../../input/{current_file}_input.txt", "r", encoding="utf-8-sig")

result = []
T = int(input())
for case in range(1, T + 1):
    A, B, C = map(int, input().split())
    ans = 0
    if C <= 2:
        result.append(f"#{case} -1")
        continue

    if B >= C:
        ans += B - C + 1
        B = C - 1
    if B == 1:
        result.append(f"#{case} -1")
        continue

    if A >= B:
        ans += A - B + 1
        A = B - 1
    result.append(f"#{case} {ans}")

for _ in result:
    print(_)

check_answer(current_file,result)

output = open(f"../../input/{current_file}_output.txt", "r").readlines()
output = [line.strip() for line in output]

print("------------------- 오답 ------------------ ( 이 아래로 출력이 없으면 정답)")

for r, o in zip(result, output):
    if r != o:
        print(f"정답 : {o},     오답 : {r}")
