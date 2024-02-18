import os
import sys

current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"input/{current_file}_input.txt", "r")

result = []


for case in range(1, 10 + 1):
    N = int(input())
    arr = list(list(map(int, input().split())) for _ in range(N))
    visited = list([False] * 100 for _ in range(100))
    cnt = 0
    move = True

    while move:
        move = False
        # S극 move
        for i in range(1, N):
            for j in range(N):
                if arr[i][j] == 0 and arr[i - 1][j] == 1:
                    arr[i][j] = 1
                    arr[i - 1][j] = 0
                    move = True

        # S극 끝단 제거
        for i in range(N):
            if arr[99][i] == 1:
                arr[99][i] = 0

        # N극 move
        for i in range(N - 2, -1, -1):
            for j in range(N):
                if arr[i][j] == 0 and arr[i + 1][j] == 2:
                    arr[i][j] = 2
                    arr[i + 1][j] = 0
                    move = True

        # N극 끝단 제거
        for i in range(N):
            if arr[0][i] == 2:
                arr[0][i] = 0

    for i in range(100):
        for j in range(100):
            if arr[i][j] == 1 and not visited[i][j]:
                row = 1
                visited[i][j] = True
                if arr[i+row][j] == 2:
                    visited[i+row][j] = True
                    cnt += 1
                    continue

                while arr[i + row][j] != 2:
                    visited[i + row][j] = True
                    row += 1
                visited[i+row][j] = True
                cnt += 1
                continue


    result.append(f"#{case} {cnt}")

for i in result:
    print(i)

output = open(f"output/{current_file}_output.txt", "r").readlines()
output = [line.strip() for line in output]
print(result == output)
