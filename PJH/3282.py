import os
import sys


current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"input/{current_file}_input.txt", "r")


result = []

T = int(input())


def knapsack(W, wt, val, n):
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0

            elif wt[i - 1] <= w:
                dp[i][w] = max(val[i - 1] + dp[i - 1][w - wt[i - 1]], dp[i - 1][w])

            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]


for case in range(1, T + 1):
    N, K = map(int, input().split())
    wt, val = [], []

    for _ in range(N):
        w, v = map(int, input().split())
        wt.append(w)
        val.append(v)

    result.append(f"#{case} {knapsack(K, wt, val, N)}")

for _ in result:
    print(_)


output = open(f"input/{current_file}_output.txt", "r").readlines()
output = [line.strip() for line in output]

print("------------------- 오답 ------------------ ( 이 아래로 출력이 없으면 정답)")

for r, o in zip(result, output):
    if r != o:
        print(f"정답 : {o},     오답 : {r}")
