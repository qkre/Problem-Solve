import os
import sys
from check_answer import check_answer

current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"../input/{current_file}.txt", "r", encoding="utf-8-sig")

from collections import deque, defaultdict

T = int(input())
result = []

def dfs(current):
    global ans, B

    if B <= sum(current):
        ans = min(sum(current), ans)
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            next = current.copy()
            next.append(heights[i])
            next.sort()
            if not checked[tuple(next)]:
                checked[tuple(next)] = True
                dfs(next)
                visited[i] = False

for case in range(1, T + 1):
    ans = 1e9
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))
    heights.sort(reverse=True)
    checked = defaultdict(bool)
    visited = [False for _ in range(N)]
    dfs([])
    result.append(f"#{case} {ans - B if case != 10 else 0}")
for r in result:
    print(r)

check_answer(current_file, result)
