import os
import sys
from check_answer import check_answer

current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"../input/{current_file}.txt", "r", encoding="utf-8-sig")

from collections import deque, defaultdict

result = []

for case in range(1, 10 + 1):

    N = int(input())
    S = list(map(int, input().split("+")))
    ans = sum(S)
    result.append(f"#{case} {ans}")
for r in result:
    print(r)

check_answer(current_file, result)
