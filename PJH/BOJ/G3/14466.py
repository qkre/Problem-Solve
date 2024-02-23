from sys import stdin
from collections import deque

input = stdin.readline


def bfs(visited, road, N, sr, sc):
    q = deque()
    q.append((sr, sc))
    visited[sr][sc] = True
    dr, dc = [-1, 0, 1, 0], [0, -1, 0, 1]

    while q:
        r, c = q.popleft()

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if (nr, nc) in road[r][c]:
                continue

            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                visited[nr][nc] = True
                q.append((nr, nc))


def solution():
    N, K, R = map(int, input().split())

    count = 0
    cows = []
    road = [[[] for _ in range(N)]  for _ in range(N)]

    for _ in range(R):
        r1, c1, r2, c2 = map(int, input().split())
        road[r1 - 1][c1 - 1].append((r2 - 1, c2 - 1))
        road[r2 - 1][c2 - 1].append((r1 - 1, c1 - 1))

    for _ in range(K):
        r, c = map(int, input().split())
        cows.append((r - 1, c - 1))

    for idx, cow in enumerate(cows):
        visited = [[False for _ in range(N)] for _ in range(N)]
        bfs(visited, road, N, cow[0], cow[1])

        for r, c in cows[idx + 1:]:
            if not visited[r][c]:
                count += 1

    return count


print(solution())
