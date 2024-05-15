import os
import sys
from check_answer import check_answer

current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"../input/{current_file}.txt", "r", encoding="utf-8-sig")

result = []
T = int(input())

from collections import deque

for case in range(1, T + 1):
    N = int(input())

    ans = 0

    prices = list(map(int, input().split()))
    prices = deque(prices)

    have = 0
    max_price = max(prices)
    while prices:
        now = prices.popleft()

        if max_price < now:
            continue

        if now == max_price:
            ans += have * now
            have = 0
            if prices:
                max_price = max(prices)
            continue

        have += 1
        ans -= now




    result.append(f"#{case} {ans}")

for r in result:
    print(r)

check_answer(current_file, result)
