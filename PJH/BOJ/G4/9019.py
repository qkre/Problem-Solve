import sys
from collections import deque

input = sys.stdin.readline


def solution():
    T = int(input())
    for _ in range(T):
        A, B = map(int, input().split())

        q = deque([(A, '')])

        visited = [False for _ in range(10000)]

        while q:
            now, path = q.popleft()

            if now == B:
                print(path)
                break

            D = (2 * now) % 10000
            if not visited[D]:
                visited[D] = True
                q.append((D, path + "D"))

            S = now - 1
            if S == -1:
                S = 9999
            if not visited[S]:
                visited[S] = True
                q.append((S, path + 'S'))

            L = (now % 1000 * 10) + (now // 1000)
            if not visited[L]:
                visited[L] = True
                q.append((L, path + 'L'))

            R = (now // 10) + (now % 10 * 1000)
            if not visited[R]:
                visited[R] = True
                q.append((R, path + 'R'))


solution()
