import os
import sys
from check_answer import check_answer

current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"../input/{current_file}.txt", "r", encoding="utf-8-sig")

from collections import deque, defaultdict

result = []
for case in range(1, 10 + 1):
    ans = 0

    T, N = map(int, input().split())
    arr = list(map(int, input().split()))
    graph = defaultdict(list)
    visited = defaultdict(bool)
    for i in range(0, N * 2, 2):
        visited[arr[i]] = visited[arr[i + 1]] = False
        graph[arr[i]].append(arr[i + 1])

    q = deque()
    q.append((0, 0))
    visited[0] = True
    while q:
        s, e = q.popleft()

        if e == 99:
            ans = 1
            break

        for ne in graph[e]:
            if not visited[ne]:
                visited[ne] = True
                q.append((e, ne))

    result.append(f"#{case} {round(ans)}")

for r in result:
    print(r)

check_answer(current_file, result)
