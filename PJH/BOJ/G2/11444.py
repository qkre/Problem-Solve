from sys import stdin
from collections import defaultdict

input = stdin.readline

MOD = 1000000007

dp = defaultdict(int)

dp[0] = 0
dp[1] = 1
dp[2] = 1


def fibonacci(n):
    if not dp[n]:
        if n & 1:
            fn = fibonacci(n // 2)
            fnp = fibonacci(n // 2 + 1)

            dp[n] = (fn ** 2 + fnp ** 2) % MOD
        else:
            fn = fibonacci(n // 2)
            fnm = fibonacci(n // 2 - 1)

            dp[n] = (fn * (fn + 2 * fnm)) % MOD

    return dp[n]

N = int(input())

fibonacci(N)

print(dp[N])