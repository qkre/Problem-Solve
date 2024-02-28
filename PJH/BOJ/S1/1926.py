from sys import stdin
from collections import deque

input = stdin.readline


def solution():
    N, M = map(int, input().split())

    paints = list(list(map(int, input().split())) for _ in range(N))

    count = 0
    max_paint = 0
    visited = [[False for _ in range(M)] for _ in range(N)]
    for y in range(N):
        for x in range(M):
            if not visited[y][x] and paints[y][x] == 1:
                visited[y][x] = True
                count += 1
                m = 1

                q = deque([(y, x)])

                while q:
                    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                    sy, sx = q.popleft()

                    max_paint = max(max_paint, paints[sy][sx])

                    for dx, dy in d:
                        nx, ny = sx + dx, sy + dy

                        if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx] and paints[ny][nx] == 1:
                            m += 1
                            visited[ny][nx] = True
                            paints[ny][nx] = m
                            q.append((ny, nx))

    print(count)
    print(max_paint)

solution()