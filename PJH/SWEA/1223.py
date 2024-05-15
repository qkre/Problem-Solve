import os
import sys
from check_answer import check_answer

current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"../input/{current_file}.txt", "r", encoding="utf-8-sig")

from collections import deque, defaultdict

result = []
for case in range(1, 10 + 1):
    ans = 0

    N = int(input())
    S = list(input())

    stack = []
    operators = []

    while S:
        now = S.pop(0)

        if now.isdigit():
            stack.append(int(now))
        else:
            if now == "+":
                if len(stack) >= 2:
                    while operators and operators[-1] == "*":
                        op = operators.pop()
                        num = stack.pop()
                        stack[-1] *= num
                operators.append(now)
            else:
                operators.append(now)
    while len(stack) > 1:
        num = stack.pop()
        op = operators.pop()

        if op == "+":
            stack[-1] += num
        else:
            stack[-1] *= num
    ans = stack[0]
    result.append(f"#{case} {ans}")

for r in result:
    print(r)

check_answer(current_file, result)
