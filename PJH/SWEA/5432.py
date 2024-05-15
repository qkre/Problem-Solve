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

    razer = list(input())
    razer = deque(razer)
    stack = []
    last = ""
    bar = 0
    while razer:
        now = razer.popleft()

        if now == "(":
            stack.append(now)
            last = "("
            bar += 1
        else:
            if last == ")":
                stack.pop()
            else:
                stack.pop()
                bar -= 1
                bar += len(stack)

            last = ")"
    ans = bar
    result.append(f"#{case} {ans}")
for r in result:
    print(r)

check_answer(current_file, result)
