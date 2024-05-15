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
    cnts = [0 for _ in range(400 // 2)]

    for _ in range(N):
        S, E = map(int, input().split())

        if E < S:
            S, E = E, S

        S -= 1
        E -= 1

        for i in range(S//2, E//2+1):
            cnts[i] += 1


    ans = max(cnts)


    result.append(f"#{case} {ans}")
for r in result:
    print(r)

check_answer(current_file, result)
