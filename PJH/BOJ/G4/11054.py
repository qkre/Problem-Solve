from sys import stdin

input = stdin.readline


def solution(N):
    answer = 0
    arr = [0] + list(map(int, input().split())) + [0]

    LIS = [0] * (N+2)
    LIS_R = [0] * (N+2)

    for i in range(1, N+1):
        for j in range(i):
            if arr[j] < arr[i]:
                LIS[i] = max(LIS[i], LIS[j] + 1)

    for i in range(N, 0, -1):
        for j in range(N, i, -1):
            if arr[j] < arr[i]:
                LIS_R[i] = max(LIS_R[i], LIS_R[j] + 1)


    for i in range(1, N+1):
        answer = max(answer, LIS[i] + LIS_R[i])


    print(answer)


solution(int(input()))
