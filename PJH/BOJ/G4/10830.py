from sys import stdin
from copy import deepcopy

input = stdin.readline


def solution():
    N, B = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]
    org = deepcopy(arr)
    n = deepcopy(arr)

    bin_B = format(B, 'b')


    for case in range(1, len(bin_B)):
        if bin_B[case] == '1':
            for i in range(N):
                for j in range(N):
                    temp = 0
                    for k in range(N):
                        temp += (arr[i][k] % 1000 * arr[k][j] % 1000) % 1000

                    n[i][j] = temp % 1000

            for i in range(N):
                for j in range(N):
                    arr[i][j] = n[i][j]

            for i in range(N):
                for j in range(N):
                    temp = 0
                    for k in range(N):
                        temp += (arr[i][k] % 1000 * org[k][j] % 1000) % 1000

                    n[i][j] = temp % 1000

            for i in range(N):
                for j in range(N):
                    arr[i][j] = n[i][j]

        else:
            for i in range(N):
                for j in range(N):
                    temp = 0
                    for k in range(N):
                        temp += (arr[i][k] % 1000 * arr[k][j] % 1000) % 1000

                    n[i][j] = temp % 1000

            for i in range(N):
                for j in range(N):
                    arr[i][j] = n[i][j]

    for i in range(N):
        for j in range(N):
            arr[i][j] %= 1000

    for a in arr:
        print(*a)


solution()
