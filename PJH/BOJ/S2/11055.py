from sys import stdin
input = stdin.readline

def solution():
    N = int(input())
    arr = list(map(int, input().split()))

    LIS = arr.copy()

    for i in range(N):
        for j in range(i):
            if arr[j] < arr[i] and LIS[i] < LIS[j] + arr[i]:
                LIS[i] = LIS[j] + arr[i]

    print(max(LIS))

solution()