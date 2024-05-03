import os
import sys

current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"../../input/{current_file}_input.txt", "r", encoding="utf-8-sig")

result = []
T = int(input())
for case in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)

    min_value = 10e9

    for i in range(N):
        if i+K > N:
            break
        part = arr[i:i+K]

        min_value = min(min_value, part[0] - part[-1])

    result.append(f"#{case} {min_value}")
for _ in result:
    print(_)


output = open(f"../../input/{current_file}_output.txt", "r").readlines()
output = [line.strip() for line in output]

print("------------------- 오답 ------------------ ( 이 아래로 출력이 없으면 정답)")

for r, o in zip(result, output):
    if r != o:
        print(f"정답 : {o},     오답 : {r}")
