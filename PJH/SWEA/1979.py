import sys

sys.stdin = open("input/1979_input.txt", "r")

T = int(input())


def check(direction, y, x):
    global N, K

    if direction == 0:
        if x + K > N:
            return False

        if 0 in arr[y][x : x + K]:
            return False
        elif x + K != N and arr[y][x + K] == 1:
            return False
        elif x != 0 and arr[y][x - 1] == 1:
            return False

        return True

    else:
        if y + K > N:
            return False

        for i in range(1, K):
            if arr[y + i][x] == 0:
                return False

        if y + K != N and arr[y + K][x] == 1:
            return False

        elif y != 0 and arr[y - 1][x] == 1:
            return False

        return True


for case in range(1, T + 1):
    N, K = map(int, input().split())
    cnt = 0
    arr = list(list(map(int, input().split())) for _ in range(N))

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                if check(0, i, j):
                    cnt += 1
                if check(1, i, j):
                    cnt += 1

    print(f"#{case} {cnt}")
