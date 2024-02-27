from sys import stdin
from bisect import bisect_right
input = stdin.readline


def solution(N):
    arr = list(map(int, input().split()))

    idx = [-1] * (N+1)
    longest = 0
    cnt = 1

    for i, v in enumerate(arr):
        idx[v] = i

    for num in range(1, N):
        if idx[num] < idx[num + 1]:
            cnt += 1
        else:
            longest = max(longest, cnt)
            cnt = 1

    return N - longest if N != 1 else 0


print(solution(int(input())))
