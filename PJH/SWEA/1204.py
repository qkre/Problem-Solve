import os
import sys
from check_answer import check_answer

current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"../input/{current_file}.txt", "r", encoding="utf-8-sig")

result = []
T = int(input())

from collections import Counter

for case in range(1, T + 1):
    N = int(input())
    ans = 0
    arr = list(map(int, input().split()))

    ans = Counter(arr).most_common()[0][0]



    result.append(f"#{case} {ans}")

for r in result:
    print(r)

check_answer(current_file, result)
