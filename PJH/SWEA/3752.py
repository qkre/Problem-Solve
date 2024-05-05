import os
import sys

current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"../../input/{current_file}_input.txt", "r", encoding="utf-8-sig")

result = []
T = int(input())

for case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    visited = [False for _ in range(sum(arr) + 1)]
    visited[0] = True
    for n in arr:
        for i in range(sum(arr), -1, -1):
            if visited[i]:
                visited[i + n] = True

    ans = visited.count(True)

    result.append(f"#{case} {ans}")
for _ in result:
    print(_)

output = open(f"../../input/{current_file}_output.txt", "r").readlines()
output = [line.strip() for line in output]

print("------------------- 오답 ------------------ ( 이 아래로 출력이 없으면 정답)")

for r, o in zip(result, output):
    if r != o:
        print(f"정답 : {o},     오답 : {r}")
