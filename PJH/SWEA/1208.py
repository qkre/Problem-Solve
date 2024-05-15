import os
import sys
from check_answer import check_answer

current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"../input/{current_file}.txt", "r", encoding="utf-8-sig")

result = []
for case in range(1, 10 + 1):
    ans = 0
    N = int(input())
    boxes = list(map(int, input().split()))

    for i in range(N):
        boxes[boxes.index(max(boxes))] -= 1
        boxes[boxes.index(min(boxes))] += 1

    ans = max(boxes) - min(boxes)

    result.append(f"#{case} {ans}")

for r in result:
    print(r)

check_answer(current_file, result)
