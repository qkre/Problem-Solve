from sys import stdin

input = stdin.readline


def solution():
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    answer = float('inf')

    for i in range(N):
        answer = min(answer, arr[i] + arr[N * 2 - 1 - i])

    return answer


print(solution())
