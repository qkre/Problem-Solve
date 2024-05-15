import os
import sys
from check_answer import check_answer

current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"../input/{current_file}.txt", "r", encoding="utf-8-sig")

result = []

for case in range(1, 11):
    N = int(input())

    ans = 0

    buildings = list(map(int, input().split()))

    for i in range(N):
        if buildings[i] == 0:
            continue

        else:
            left = max(buildings[i - 1], buildings[i - 2])
            right = max(buildings[i + 1], buildings[i + 2])

            ans += buildings[i] - max(left, right) if max(left, right) < buildings[i] else 0

    result.append(f"#{case} {ans}")

for r in result:
    print(r)

check_answer(current_file, result)
