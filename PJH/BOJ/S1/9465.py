from sys import stdin

input = stdin.readline

T = int(input())


def solution(T):
    for _ in range(T):
        N = int(input())
        maps = list(list(map(int, input().split())) for _ in range(2))

        dp = [[0, 0, 0] for _ in range(N)]

        dp[0][0] = maps[0][0]
        dp[0][1] = maps[1][0]

        for i in range(1, N):
            dp[i][0] = max(dp[i-1][1] + maps[0][i], dp[i-1][2] + maps[0][i])
            dp[i][1] = max(dp[i-1][0] + maps[1][i], dp[i-1][2] + maps[1][i])
            dp[i][2] = max(dp[i-1][0], dp[i-1][1])

        print(max(dp[N-1]))
solution(T)
