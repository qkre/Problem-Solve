from sys import stdin
from collections import deque

input = stdin.readline


def solution():
    R, C, K = map(int, input().split())
    maps = [list(input().rstrip()) for _ in range(R)]

    visited = [[[float('inf') for _ in range(C)] for _ in range(R)] for _ in range(K + 1)]

    for k in range(K + 1):
        visited[k][0][0] = 1

    q = deque([(0, 0, 0, True)])

    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    printed = False
    min_distance = float('inf')
    while q:
        y, x, crashed, day_light = q.popleft()

        if (y, x) == (R - 1, C - 1):
            printed = True

            for k in range(K + 1):
                min_distance = min(min_distance, visited[k][y][x])
            break

        for dx, dy in d:
            ny, nx = y + dy, x + dx
            new_cost = visited[crashed][y][x] + 1

            if 0 <= ny < R and 0 <= nx < C:
                if crashed == K and maps[ny][nx] != '1':
                    if new_cost < visited[crashed][ny][nx]:
                        visited[crashed][ny][nx] = new_cost
                        q.append((ny, nx, crashed, not day_light))
                elif crashed < K:
                    if maps[ny][nx] == '1':
                        if day_light:
                            if new_cost < visited[crashed + 1][ny][nx]:
                                visited[crashed + 1][ny][nx] = new_cost
                                q.append((ny, nx, crashed + 1, not day_light))
                        else:
                            visited[crashed][ny][nx] = new_cost + 1
                            q.append((ny, nx, crashed, not day_light))

                    else:
                        if new_cost < visited[crashed][ny][nx]:
                            visited[crashed][ny][nx] = new_cost
                            q.append((ny, nx, crashed, not day_light))
    if printed:
        print(min_distance)

    if not printed:
        print(-1)


solution()
