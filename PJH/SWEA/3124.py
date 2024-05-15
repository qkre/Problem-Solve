import os
import sys
from check_answer import check_answer

current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"../input/{current_file}.txt", "r", encoding="utf-8-sig")

from collections import deque, defaultdict
from heapq import heappop, heappush

result = []
T = int(input())

def find(v):
    if root[v] != v:
        return find(root[v])
    return v

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        root[b] = root[a]
    else:
        root[a] = root[b]

for case in range(1, T + 1):
    ans = 0
    V, E = map(int, input().split())
    root = [i for i in range(V+1)]
    pq = []
    for _ in range(E):
        A, B, C = map(int, input().split())
        heappush(pq, (C, A, B))

    while pq:
        cost, s, e = heappop(pq)
        if find(s) != find(e):
            ans += cost
            union(s, e)

    result.append(f"#{case} {ans}")
for r in result:
    print(r)

check_answer(current_file, result)
