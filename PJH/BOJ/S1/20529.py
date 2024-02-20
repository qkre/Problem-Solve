from sys import stdin
from collections import deque

input = stdin.readline


def solution():
    T = int(input())
    for _ in range(T):
        answer = 2e9
        N = int(input())
        arr = list(input().split())
        if len(arr) >= 48:
            print(0)
            continue

        for i in range(N):
            for j in range(i + 1, N):
                for k in range(j + 1, N):
                    A = arr[i]
                    B = arr[j]
                    C = arr[k]

                    distance_AB = 0
                    distance_BC = 0
                    distance_AC = 0

                    if A != B:
                        for l in range(4):
                            if A[l] != B[l]:
                                distance_AB += 1
                    if B != C:
                        for l in range(4):
                            if B[l] != C[l]:
                                distance_BC += 1

                    if A != C:
                        for l in range(4):
                            if A[l] != C[l]:
                                distance_AC += 1

                    answer = min(answer, distance_AB + distance_BC + distance_AC)

        print(answer)


solution()
