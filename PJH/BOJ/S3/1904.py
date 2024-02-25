def solution(N):
    dp = [0] * 1000001

    mod = 15746

    dp[0]= 0
    dp[1] = 1
    dp[2] = 2

    for i in range(3, N + 1):
        dp[i] = (dp[i-1] % mod + dp[i-2] % mod) % mod

    print(dp[N])

solution(int(input()))
