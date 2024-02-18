import sys

sys.stdin = open("input/2005_input.txt", "r")

T = int(input())
result = []


for case in range(1, T + 1):
    N = int(input())

    arr = list([1 for j in range(i)] for i in range(1, N + 1))

    for i in range(2, N):
        for j in range(i + 1):
            if j == 0 or j == i:
                arr[i][j] = 1
            else:
                arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j]

    print(f"#{case}")
    for i in arr:
        for j in i:
            print(j, end=" ")
        print()
