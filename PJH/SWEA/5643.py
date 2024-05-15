import os
import sys
from check_answer import check_answer

current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"../input/{current_file}.txt", "r", encoding="utf-8-sig")

from collections import deque, defaultdict

T = int(input())
result = []

for case in range(1, T + 1):
    ans = 0

    N = int(input())
    M = int(input())

    graph = [[] for _ in range(N + 1)]

    small = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    tall = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

    for _ in range(M):
        S, E = map(int, input().split())
        graph[S].append(E)

    for start in range(1, N + 1):
        visited = [False for _ in range(N + 1)]
        q = deque()
        q.append(start)

        while q:
            now = q.popleft()

            for next in graph[now]:
                if not visited[next]:
                    visited[next] = True
                    small[start][next] = small[now][next] = 1
                    tall[next][now] = tall[next][start] = 1
                    q.append(next)

    for i in range(1, N+1):
        if small[i].count(1) + tall[i].count(1) == N-1:
            ans += 1

    result.append(f"#{case} {ans}")
for r in result:
    print(r)

check_answer(current_file, result)
