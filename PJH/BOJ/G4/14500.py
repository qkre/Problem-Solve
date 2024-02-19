from sys import stdin

input = stdin.readline

answer = 0


def dfs(depth, N, M, arr, x, y, path):
    global answer
    if depth == 4:
        path_sum = 0
        for x, y in path:
            path_sum += arr[y][x]
        answer = max(answer, path_sum)
        return

    dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]

    for i in range(4):
        nx, ny = dx[i] + x, dy[i] + y

        if 0 <= nx < M and 0 <= ny < N and (nx, ny) not in path:
            path.append((nx, ny))
            dfs(depth + 1, N, M, arr, nx, ny, path)
            path.pop()


def check_woo(N, M, arr):
    global answer
    dirs = [[(0, 0), (0, 1), (0, 2), (1, 1)],  # ㅜ
            [(0, 0), (0, 1), (0, 2), (-1, 1)],  # ㅗ
            [(0, 0), (1, 0), (2, 0), (1, 1)],  # ㅏ
            [(0, 0), (1, 0), (2, 0), (1, -1)]]  # ㅓ

    for y in range(N):
        for x in range(M):
            for d1, d2, d3, d4 in dirs:
                y1, x1, y2, x2, y3, x3, y4, x4 = (
                    y + d1[0], x + d1[1], y + d2[0], x + d2[1], y + d3[0], x + d3[1], y + d4[0], x + d4[1])

                if (0 <= x1 < M and 0 <= x2 < M and 0 <= x3 < M and 0 <= x4 < M) and (
                        0 <= y1 < N and 0 <= y2 < N and 0 <= y3 < N and 0 <= y4 < N):
                    answer = max(answer, sum([arr[y1][x1], arr[y2][x2], arr[y3][x3], arr[y4][x4]]))


def solution():
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    for y in range(N):
        for x in range(M):
            dfs(1, N, M, arr, x, y, [(x, y)])

    check_woo(N, M, arr)

solution()
print(answer)
