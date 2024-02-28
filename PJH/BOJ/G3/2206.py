from sys import stdin
from collections import deque

input = stdin.readline

def solution():
    R, C = map(int, input().split())
    maps = [list(input().rstrip()) for _ in range(R)]
    not_crashed_visit = [[float('inf') for _ in range(C)] for _ in range(R)]
    crashed_visit = [[float('inf') for _ in range(C)] for _ in range(R)]
    not_crashed_visit[0][0] = crashed_visit[0][0] = 1
    q = deque([(0, 0, False)])

    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    printed = False

    while q:
        y, x, crashed = q.popleft()

        if (y, x) == (R-1, C-1):
            printed = True
            print(min(not_crashed_visit[y][x], crashed_visit[y][x]))
            break

        for dx, dy in d:
            ny, nx = y + dy, x + dx

            if crashed:
                new_cost = crashed_visit[y][x] + 1
            else:
                new_cost = not_crashed_visit[y][x] + 1

            if 0 <= ny < R and 0 <= nx < C:
                if crashed and maps[ny][nx] != '1':
                    if new_cost < crashed_visit[ny][nx]:
                        crashed_visit[ny][nx] = new_cost
                        q.append((ny, nx, crashed))

                elif not crashed:
                    if maps[ny][nx] == '1':
                        if new_cost < crashed_visit[ny][nx]:
                            crashed_visit[ny][nx] = new_cost
                            q.append((ny, nx, True))
                    else:
                        if new_cost < not_crashed_visit[ny][nx]:
                            not_crashed_visit[ny][nx] = new_cost
                            q.append((ny, nx, crashed))


    if not printed:
        print(-1)

solution()



