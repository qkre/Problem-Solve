import os
import sys
from check_answer import check_answer

current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"../input/{current_file}.txt", "r", encoding="utf-8-sig")

from collections import deque

result = []

for case in range(1, 10 + 1):
    ans = 1
    N = int(input())

    S = deque(list(input()))
    stack = []
    while S:
        now = S.popleft()

        if now in "([{<":
            stack.append(now)
        elif stack:
            if now == ")":
                if stack[-1] != "(":
                    ans = 0
                    break
                else:
                    stack.pop()
            elif now == "]":
                if stack[-1] != "[":
                    ans = 0
                    break
                else:
                    stack.pop()
            elif now == "}":
                if stack[-1] != "{":
                    ans = 0
                    break
                else:
                    stack.pop()
            elif now == ">":
                if stack[-1] != "<":
                    ans = 0
                    break
                else:
                    stack.pop()
        else:
            ans = 0
            break

    result.append(f"#{case} {ans}")

for r in result:
    print(r)

check_answer(current_file, result)
