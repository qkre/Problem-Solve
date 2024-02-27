from sys import stdin
from bisect import bisect_left

input = stdin.readline

def solution(N):
    arr = list(map(int, input().split()))

    dp = [arr[0]]

    for num in arr[1:]:
        if dp[-1] < num:
            dp.append(num)
        else:
            dp[bisect_left(dp, num)] = num

    print(len(dp))


solution(int(input()))
