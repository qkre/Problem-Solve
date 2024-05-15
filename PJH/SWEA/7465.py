import os
import sys
from check_answer import check_answer

current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"../input/{current_file}.txt", "r", encoding="utf-8-sig")

from collections import deque, defaultdict

T = int(input())
result = []

def find(v):
    if v != root[v]:
        v = find(root[v])
    return root[v]

def union(a, b):
    p_a = find(a)
    p_b = find(b)

    if p_a < p_b:
        root[p_b] = root[p_a]
    else:
        root[p_a] = root[p_b]

for case in range(1, T + 1):
    N, M = map(int, input().split())

    graph = defaultdict(list)
    root = [_ for _ in range(N + 1)]
    for _ in range(M):
        A, B = map(int, input().split())
        if find(A) == find(B):
            continue
        union(A, B)

    ans = set()
    for i in range(1, N+1):
        ans.add(find(i))

    result.append(f"#{case} {len(ans)}")
for r in result:
    print(r)

check_answer(current_file, result)
