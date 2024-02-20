from sys import stdin
from collections import deque

input = stdin.readline

def solution():
    answer = 0
    N, M = map(int, input().split())
    campus = [list(input()) for _ in range(N)]
    visited = [[False for _ in range(M)] for _ in range(N)]
    q = deque()
    for y in range(N):
        for x in range(M):
            if campus[y][x] == 'I':
                q.append((y, x))
                break
        if q:
            break

    while q:
        y, x = q.popleft()

        dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0<= nx < M and 0 <= ny < N and campus[ny][nx] != 'X' and not visited[ny][nx]:
                visited[ny][nx] = True
                if campus[ny][nx] == 'P':
                    answer += 1
                q.append((ny, nx))

    if answer == 0:
        answer = 'TT'

    print(answer)

solution()