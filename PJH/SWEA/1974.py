import sys

sys.stdin = open("input/1974_input.txt", "r")

T = int(input())


def box_check(y, x):
    global N

    visited = [False for _ in range(10)]

    for i in range(3):
        for j in range(3):
            if visited[arr[y + i][x + j]]:
                return False
            else:
                visited[arr[y + i][x + j]] = True

    return True


def check(direction, y, x):
    if direction == 0:
        for i in range(1, 10):
            if 1 != arr[y].count(i):
                return False

    if direction == 1:
        visited = [False for _ in range(10)]
        for i in range(9):
            if visited[arr[i][x]]:
                return False
            else:
                visited[arr[i][x]] = True

    return True


for case in range(1, T + 1):
    arr = list(list(map(int, input().split())) for _ in range(9))
    ans = 1

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if not box_check(i, j):
                ans = 0
                break

    for i in range(9):
        if not check(0, i, 0):
            ans = 0
        if not check(1, 0, i):
            ans = 0

    print(f"#{case} {ans}")
