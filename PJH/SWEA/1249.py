import sys

sys.stdin = open("input/1249_input.txt", "r")

T = int(input())

INF = 10**5


def bfs(si, sj, ei, ej):
    q = []
    v = [[INF] * N for _ in range(N)]

    q.append((si, sj))
    v[si][sj] = arr[si][sj]

    while q:
        ci, cj = q.pop(0)

        # 네 방향, 범위 내 중복 허용 (이동할 위치보다 더 적은 비용만)
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj

            if 0 <= ni < N and 0 <= nj < N and v[ni][nj] > v[ci][cj] + arr[ni][nj]:
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] + arr[ni][nj]

    return v[ei][ej]


for case in range(1, T + 1):
    N = int(input())

    arr = [list(map(int, input())) for _ in range(N)]

    ans = bfs(0, 0, N - 1, N - 1)

    print(f"#{case} {ans}")
