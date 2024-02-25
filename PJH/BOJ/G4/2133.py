from sys import stdin
input = stdin.readline

def solution(N):
    dp = [0] * (N+1)
    dp[2] = 3
    for i in range(4, N+1, 2):
        if i % 4 == 0:
            dp[i] = dp[i-2] * 3 + i // 2
        else:
            dp[i] = dp[i-2] * 3

    return dp[N]

print(solution(int(input())))