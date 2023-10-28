import sys

sys.stdin = open("input/2005_input.txt")

t = int(input())

for c in range(t):
    n = int(input())
    arr = [[1] * i for i in range(1, n + 1)]

    for i in range(2, n):
        for j in range(1, i):
            arr[i][i - j] = arr[i - 1][i - j - 1] + arr[i - 1][i - j]

    print(f"#{c + 1}")
    for i in arr:
        print(*i, end="\n")
