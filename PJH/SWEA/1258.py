import os
import sys
from check_answer import check_answer

current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"../input/{current_file}.txt", "r", encoding="utf-8-sig")

from collections import deque, defaultdict
from heapq import heappop, heappush

result = []
T = int(input())


def bfs(r, c):
    global N
    q = deque([(r, c)])
    visited[r][c] = True
    min_row = max_row = r
    min_col = max_col = c

    while q:
        r, c = q.popleft()

        min_row = min(r, min_row)
        max_row = max(r, max_row)
        min_col = min(c, min_col)
        max_col = max(c, max_col)

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc

            if 0 <= nr < N and 0 <= nc < N:
                if maps[nr][nc] != 0:
                    if not visited[nr][nc]:
                        visited[nr][nc] = True
                        q.append((nr, nc))

    R = max_row - min_row + 1
    C = max_col - min_col + 1

    return (R * C, R, C)


for case in range(1, T + 1):
    ans = []
    N = int(input())
    maps = list(list(map(int, input().split())) for _ in range(N))
    visited = [[False for _ in range(N)] for _ in range(N)]
    pq = []

    for r in range(N):
        for c in range(N):
            if maps[r][c] and not visited[r][c]:
                pq.append(bfs(r, c))

    pq.sort(key= lambda x: (x[0], x[1], x[2]))

    ans.append(len(pq))
    for size, row, col in pq:
        ans.append(row)
        ans.append(col)

    ans = ' '.join(list(map(str, ans)))
    result.append(f"#{case} {ans}")
for r in result:
    print(r)

check_answer(current_file, result)
