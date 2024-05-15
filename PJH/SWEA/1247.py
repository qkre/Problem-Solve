import os
import sys
from check_answer import check_answer

current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"../input/{current_file}.txt", "r", encoding="utf-8-sig")

from collections import deque, defaultdict
from heapq import heappop, heappush
from itertools import permutations

result = []
T = int(input())

for case in range(1, T + 1):
    ans = 0
    N = int(input())
    root = [i for i in range(N + 1)]
    ls = list(map(int, input().split()))
    weights = [[0 for _ in range(N + 2)] for _ in range(N + 2)]

    for i in range(0, (N + 2) * 2, 2):
        for j in range(0, (N + 2) * 2, 2):
            if i == j:
                continue
            weights[i//2][j//2] = abs(ls[i] - ls[j]) + abs(ls[i + 1] - ls[j + 1])

    print(weights)

    result.append(f"#{case} {ans}")

for r in result:
    print(r)

check_answer(current_file, result)
