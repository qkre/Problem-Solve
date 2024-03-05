from sys import stdin
from copy import deepcopy

input = stdin.readline

def times(arr, target, N):

    answer = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            for k in range(N):
                answer[i][j] += (arr[i][k] % 1000 * target[k][j] % 1000) % 1000

    return answer

def solution():
    N, B = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]
    org = deepcopy(arr)

    bin_B = format(B, 'b')


    for case in range(1, len(bin_B)):
        if bin_B[case] == '1':
            arr = times(arr, arr, N)
            arr = times(arr, org, N)

        else:
            arr = times(arr, arr, N)


    for i in range(N):
        for j in range(N):
            arr[i][j] %= 1000

    for a in arr:
        print(*a)


solution()
