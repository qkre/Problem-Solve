import sys

sys.stdin = open("input/2001_input.txt", "r")

T = int(input())

for case in range(1, T + 1):
    N, M = map(int, input().split())

    arr = list(list(map(int, input().split())) for _ in range(N))

    ans = 0

    if N == M:
        print(f"#{case} {sum(arr)}")

    for y in range(N - M + 1):
        for x in range(N - M + 1):
            temp = 0

            for i in range(M):
                for j in range(M):
                    temp += arr[y + i][x + j]

            ans = max(ans, temp)

    print(f"#{case} {ans}")
