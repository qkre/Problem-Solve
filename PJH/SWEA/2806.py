import sys

sys.stdin = open("input/2806_input.txt", "r")

T = int(input())


def check(y, x, possible):
    if True in possible[y]:
        return False

    for i in range(y + 1):
        if possible[y - i][x]:
            return False

    for i in range(1, y + 1):
        if 0 <= y - i and 0 <= x - i:
            if possible[y - i][x - i]:
                return False
        if 0 <= y - i and x + i < N:
            if possible[y - i][x + i]:
                return False

    return True


def dfs(depth, cnt, possible):
    global N, ans
    if depth == N and cnt == N:
        ans += 1
        return

    for i in range(N):
        if check(depth, i, possible):
            possible[depth][i] = True
            dfs(depth + 1, cnt + 1, possible)
            possible[depth][i] = False


for case in range(1, T + 1):
    N = int(input())

    arr = list([0] * N for _ in range(N))
    possible = list([False] * N for _ in range(N))
    ans = 0
    for i in range(N):
        possible[0][i] = True
        dfs(1, 1, possible)
        possible[0][i] = False

    print(f"#{case} {ans}")
