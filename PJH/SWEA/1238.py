import os
import sys

current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"../../input/{current_file}_input.txt", "r", encoding="utf-8-sig")

from collections import deque, defaultdict
result = []
for case in range(1, 11):
    ans = 0

    N, S = map(int, input().split())

    graph = defaultdict(set)

    ls = list(map(int, input().split()))

    for i in range(0, N, 2):
        graph[ls[i]].add(ls[i+1])

    visited = defaultdict(bool)
    visited[S] = True
    q = deque()
    q.append((0, S))
    max_depth = 0
    while q:
        depth, caller = q.popleft()

        if max_depth < depth:
            ans = caller
            max_depth = depth
        elif max_depth == depth:
            ans = max(ans, caller)

        for receiver in graph[caller]:
            if not visited[receiver]:
                visited[receiver] = True
                q.append((depth + 1, receiver))




    result.append(f"#{case} {ans}")
for _ in result:
    print(_)

output = open(f"../../input/{current_file}_output.txt", "r").readlines()
output = [line.strip() for line in output]

print("------------------- 오답 ------------------ ( 이 아래로 출력이 없으면 정답)")

for y, o in zip(result, output):
    if y != o:
        print(f"정답 : {o},     오답 : {y}")
