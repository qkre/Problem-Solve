from sys import stdin
from collections import deque

input = stdin.readline

M, N, H = map(int, input().split())
tomatoes = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]


def solution(M, N, H, tomatoes):
    q = deque()
    visited = [[[False for _ in range(M)] for _ in range(N)] for _ in range(H)]
    days = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]

    for h in range(H):
        for y in range(N):
            for x in range(M):
                if tomatoes[h][y][x] == 1:
                    q.append((h, y, x))


    while q:
        h, y, x = q.popleft()
        visited[h][y][x] = True
        dx, dy, dh = [-1, 0, 1, 0, 0, 0], [0, -1, 0, 1, 0, 0], [0, 0, 0, 0, -1, 1]

        for i in range(6):
            nx, ny, nh = dx[i] + x, dy[i] + y, dh[i] + h

            if (0 <= nx < M and 0 <= ny < N and 0 <= nh < H) and not visited[nh][ny][nx] and tomatoes[nh][ny][nx] == 0:
                days[nh][ny][nx] = days[h][y][x] + 1
                tomatoes[nh][ny][nx] = 1
                q.append((nh, ny, nx))

    max_days = 0

    for h in range(H):
        for tomato in tomatoes[h]:
            if 0 in tomato:
                return -1

        for day in days[h]:
            max_days = max(max_days, max(day))

    return max_days


print(solution(M, N, H, tomatoes))
