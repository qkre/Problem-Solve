import sys

sys.stdin = open("./input/1961_input.txt")

t = int(input())

for c in range(t):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    arr90 = [[0 for _ in range(n)] for __ in range(n)]
    arr180 = [[0 for _ in range(n)] for __ in range(n)]
    arr270 = [[0 for _ in range(n)] for __ in range(n)]
    ret = [[0 for _ in range(n)] for __ in range(n)]

    for i in range(n):
        for j in range(n):
            arr90[i][j] = arr[n - 1 - j][i]

    for i in range(n):
        for j in range(n):
            arr180[i][j] = arr[n - 1 - i][n - 1 - j]

    for i in range(n):
        for j in range(n):
            arr270[i][j] = arr[j][n - 1 - i]

    for k in range(n):
        for i in range(n):
            temp = ""

            if k == 0:
                for j in range(n):
                    temp += str(arr90[i][j])
                ret[i][k] = temp
            elif k == 1:
                for j in range(n):
                    temp += str(arr180[i][j])
                ret[i][k] = temp

            elif k == 2:
                for j in range(n):
                    temp += str(arr270[i][j])
                ret[i][k] = temp
    print(f"#{c+1}")
    for i in range(n):
        for j in range(3):
            print(ret[i][j], end=" ")
        print()
