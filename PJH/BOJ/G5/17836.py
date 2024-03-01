from sys import stdin
from collections import deque

input = stdin.readline

N, M, T = map(int, input().split())
maps = list(list(map(int, input().split())) for _ in range(N))


def solution(N, M, T, maps):
    D = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    sword = ()
    for r in range(N):
        for c in range(M):
            if maps[r][c] == 2:
                sword = (r, c)

    dijkstra = [[[float('inf') for _ in range(M)] for _ in range(N)] for _ in range(2)]
    dijkstra[0][0][0] = dijkstra[1][0][0] = 0

    q = deque([(0, 0, 0, False)])

    while q:
        r, c, cost, s = q.popleft()
        if (r, c) == sword:
            s = True
        for dr, dc in D:
            nr, nc = dr + r, dc + c

            if 0 <= nr < N and 0 <= nc < M:
                if (nr, nc) == sword:
                    if dijkstra[1][nr][nc] > cost + 1:
                        dijkstra[1][nr][nc] = cost + 1
                        q.append((nr, nc, cost + 1, True))
                else:
                    if s:
                        if dijkstra[1][nr][nc] > cost + 1:
                            dijkstra[1][nr][nc] = cost + 1
                            q.append((nr, nc, cost + 1, s))
                    if not s and maps[nr][nc] == 0:
                        if dijkstra[0][nr][nc] > cost + 1:
                            dijkstra[0][nr][nc] = cost + 1
                            q.append((nr, nc, cost + 1, s))

    ans = min(dijkstra[0][-1][-1], dijkstra[1][-1][-1])

    if ans <= T:
        print(ans)
    else:
        print("Fail")

solution(N, M, T, maps)