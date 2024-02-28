from sys import stdin
from collections import deque

input = stdin.readline


def solution(N):
    for case in range(N):
        C, R = map(int, input().split())

        maze = list(list(input().rstrip()) for _ in range(R))

        jihoon = ()
        fires = deque()
        for y in range(R):
            for x in range(C):
                if maze[y][x] == '@':
                    jihoon = (y, x)
                elif maze[y][x] == '*':
                    fires.append((y, x))

        visited = [[False for _ in range(C)] for _ in range(R)]
        visited[jihoon[0]][jihoon[1]] = True
        q = deque([jihoon])
        d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        ans = 0
        escaped = False
        while q:
            if escaped:
                break

            fires_len = len(fires)

            for i in range(fires_len):
                fy, fx = fires.popleft()
                visited[fy][fx] = True
                for dx, dy in d:
                    nx, ny = fx + dx, fy + dy

                    if 0 <= nx < C and 0 <= ny < R and maze[ny][nx] != '*' and maze[ny][nx] != '#':
                        maze[ny][nx] = '*'
                        visited[ny][nx] = True
                        fires.append((ny, nx))

            jihoon_len = len(q)

            for i in range(jihoon_len):
                sy, sx = q.popleft()

                if sy == 0 or sy == R - 1 or sx == 0 or sx == C - 1:
                    print(ans + 1)
                    escaped = True
                    break

                for dx, dy in d:
                    nx, ny = sx + dx, sy + dy

                    if 0 <= nx < C and 0 <= ny < R and maze[ny][nx] != '#' and not visited[ny][nx]:
                        visited[ny][nx] = True
                        maze[ny][nx] = '@'
                        q.append((ny, nx))
            ans += 1

        if not escaped:
            print("IMPOSSIBLE")


solution(int(input()))
