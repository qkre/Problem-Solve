from collections import deque

R, C = map(int, input().split())
maps = list(list(input()) for _ in range(R))
ans = 0
def bfs(r, c):
    global R, C
    dijkstra = [[float("inf") for _ in range(C)] for _ in range(R)]
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    dijkstra[r][c] = 0

    q = deque([(r, c)])

    while q:
        r, c = q.popleft()

        for dr, dc in d:
            nr, nc = r + dr, c + dc

            if 0 <= nr < R and 0 <= nc < C and maps[nr][nc] == "L":
                cost = dijkstra[r][c] + 1

                if cost < dijkstra[nr][nc]:
                    dijkstra[nr][nc] = cost
                    q.append((nr, nc))

    max_length = 0

    for r in range(R):
        for c in range(C):
            if dijkstra[r][c] != float('inf') and dijkstra[r][c] > max_length:
                max_length = dijkstra[r][c]

    return max_length

for r in range(R):
    for c in range(C):
        if maps[r][c] == "L":
            ans = max(ans, bfs(r, c))

print(ans)