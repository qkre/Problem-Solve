import os
import sys

current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"../../input/{current_file}_input.txt", "r", encoding="utf-8-sig")


def dfs(depth):
    global ans

    if depth == M:
        ans = max(ans, int(''.join(arr)))
        return

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            arr[i], arr[j] = arr[j], arr[i]

            check = int(''.join(arr))
            if (depth, check) not in visited:
                visited.append((depth, check))
                dfs(depth + 1)

            arr[i], arr[j] = arr[j], arr[i]


result = []
T = int(input())
for case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(str(N))
    visited = []
    ans = 0
    dfs(0)

    result.append(f"#{case} {ans}")
for _ in result:
    print(_)

output = open(f"../../input/{current_file}_output.txt", "r").readlines()
output = [line.strip() for line in output]

print("------------------- 오답 ------------------ ( 이 아래로 출력이 없으면 정답)")

for r, o in zip(result, output):
    if r != o:
        print(f"정답 : {o},     오답 : {r}")
