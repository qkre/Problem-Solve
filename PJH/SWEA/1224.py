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
    S = deque(list(input()))
    stack = []
    op = []
    while S:
        now = S.popleft()

        if now.isdigit():
            stack.append(int(now))
        elif now == "(":
            stack.append(now)
        else:
            if now == "+":
                while op and op[-1] == "*":
                    if len(stack) < 2:
                        break
                    if stack[-2] == "(":
                        break

                    num = stack.pop()
                    op.pop()
                    stack[-1] *= num

                op.append(now)
            elif now == "*":
                op.append(now)
            else:
                while stack and stack[-1] != "(":
                    num = stack.pop()

                    if stack[-1] == "(":
                        stack.pop()
                        stack.append(num)
                        break

                    operator = op.pop()
                    if operator == "+":
                        stack[-1] += num
                    else:
                        stack[-1] *= num


    ans = stack[0]

    result.append(f"#{case} {ans}")

for r in result:
    print(r)

check_answer(current_file, result)
