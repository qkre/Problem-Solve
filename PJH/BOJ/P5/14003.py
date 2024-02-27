from sys import stdin
from bisect import bisect_left

input = stdin.readline


def solution(N):
    arr = list(map(int, input().split()))

    dp = [arr[0]]
    record = [-1] * N
    record[0] = 0
    for i in range(1, N):
        if dp[-1] < arr[i]:
            record[i] = len(dp)
            dp.append(arr[i])


        else:
            record[i] = bisect_left(dp, arr[i])
            dp[bisect_left(dp, arr[i])] = arr[i]

    stack = []
    idx = len(dp) - 1
    for i in range(N - 1, -1, -1):
        if record[i] == idx:
            idx -= 1
            stack.append(arr[i])

    print(len(dp))
    print(*reversed(stack))


solution(int(input()))
