import os
import sys
from test import check_answer

current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"../../input/{current_file}_input.txt", "r", encoding="utf-8-sig")

result = []
T = int(input())
for case in range(1, T + 1):
    a, b, c = map(int, input().split())
    x = abs((b-a) - (c-b)) / 2

    result.append(f"#{case} {x:.1f}")

for _ in result:
    print(_)

check_answer(current_file, result)
