import os
import sys

current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"input/{current_file}_input.txt", "r")

result = []

T = int(input())


def dfs(c, index):
    global N, K, cnt

    if index == N+1 or c > K:
        return
    elif c == K:
        cnt += 1
        return

    for i in range(index, N):
        dfs(c + A[i], i + 1)


for case in range(1, T + 1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    cnt = 0
    for i in range(N):
        dfs(A[i], i + 1)

    result.append(f"#{case} {cnt}")

for i in result:
    print(i)

output = open(f"output/{current_file}_output.txt", "r").readlines()
output = [line.strip() for line in output]
print(result == output)
