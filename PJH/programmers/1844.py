def solution(maps):
    w = len(maps[0])
    h = len(maps)

    visited = [[False for _ in range(w)] for _ in range(h)]

    import heapq

    q = [(0, 0, 1)]
    visited[0][0] = True
    while q:
        x, y, cost = heapq.heappop(q)

        dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]

        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if (0 <= nx < w and 0 <= ny < h) and maps[ny][nx] != 0:
                if visited[ny][nx]:
                    if cost + 1 < maps[ny][nx]:
                        maps[ny][nx] = cost + 1
                        heapq.heappush(q, (nx, ny, cost + 1))
                else:
                    visited[ny][nx] = True
                    maps[ny][nx] = cost + 1
                    heapq.heappush(q, (nx, ny, cost + 1))

    if visited[-1][-1]:
        answer = maps[-1][-1]
    else:
        answer = -1

    return answer


print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))
