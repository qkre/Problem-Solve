from sys import stdin
from collections import deque

input = stdin.readline


def solution():
    N, M = map(int, input().split())
    ladders = [list(map(int, input().split())) for _ in range(N)]
    ladders.sort()
    snakes = [list(map(int, input().split())) for _ in range(M)]
    snakes.sort()
    visited = [False] * 101
    q = deque([(1, 0)])
    visited[1] = True
    while q:
        now, cnt = q.popleft()

        if now == 100:
            print(cnt)
            break

        for i in range(1, 7):
            if now + i > 100:
                break
            moved = False
            for ladder in ladders:
                if ladder[0] == now + i:
                    visited[ladder[1]] = True
                    q.append((ladder[1], cnt + 1))
                    moved = True
                    break

            if moved:
                continue

            for snake in snakes:
                if snake[0] == (now + i):
                    visited[snake[1]] = True
                    q.append((snake[1], cnt + 1))
                    moved = True
                    break

            if moved:
                continue

            if not visited[now + i]:
                visited[now + i] = True
                q.append((now + i, cnt + 1))


solution()
