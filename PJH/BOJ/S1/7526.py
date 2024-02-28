from sys import stdin
from collections import deque

input = stdin.readline


def solution(N):
    d = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]

    for case in range(N):
        I = int(input())
        board = [['.' for _ in range(I)] for _ in range(I)]
        visited = [[False for _ in range(I)] for _ in range(I)]
        y, x = map(int, input().split())
        visited[y][x] = True
        board[y][x] = 'N'

        target = tuple(map(int, input().split()))

        q = deque([(y, x, 0)])
        while q:
            y, x, ans = q.popleft()

            if (y, x) == target:
                print(ans)
                break

            for dx, dy in d:
                ny, nx = y + dy, x + dx

                if 0 <= ny < I and 0 <= nx < I and not visited[ny][nx]:
                    visited[ny][nx] = True
                    q.append((ny, nx, ans + 1))


solution(int(input()))
