import sys

sys.stdin = open("input/1979_input.txt")

t = int(input())

for c in range(t):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    ret = 0

    # 가로
    for i in range(n):
        cnt = 0
        for j in range(n):
            if arr[i][j] == 1:
                cnt += 1
            if arr[i][j] == 0 or j == n - 1:
                if cnt == k:
                    ret += 1
                if arr[i][j] == 0:
                    cnt = 0

    # 세로
    for i in range(n):
        cnt = 0
        for j in range(n):
            if arr[j][i] == 1:
                cnt += 1
            if arr[j][i] == 0 or j == n - 1:
                if cnt == k:
                    ret += 1
                if arr[j][i] == 0:
                    cnt = 0

    print(f"#{c+1} {ret}")
