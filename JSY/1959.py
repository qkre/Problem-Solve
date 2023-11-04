import sys

sys.stdin = open("./input/1959_input.txt")
t = int(input())

for c in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ret = []

    if n < m:
        for i in range(m - n + 1):
            temp = 0
            for j in range(n):
                temp += a[j] * b[i + j]
            ret.append(temp)

    else:
        for i in range(n - m + 1):
            temp = 0
            for j in range(m):
                temp += a[i + j] * b[j]
            ret.append(temp)

    print(f"#{c+1} {max(ret)}")
