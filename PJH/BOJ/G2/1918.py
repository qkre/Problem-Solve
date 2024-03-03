from sys import stdin
from collections import deque

input = stdin.readline


def solution(exp):
    stack = []
    postorder = []

    exp = deque(exp)

    while exp:
        s = exp.popleft()

        if s in "+-*/()":
            if s == '(':
                stack.append(s)
            elif s == ")":
                while stack[-1] != '(':
                    postorder.append(stack.pop())
                stack.pop()
            else:
                if s in "*/":
                    while stack and stack[-1] in "*/":
                        postorder.append(stack.pop())
                    stack.append(s)
                else:
                    while stack and stack[-1] != "(":
                        postorder.append(stack.pop())
                    stack.append(s)
        else:
            postorder.append(s)

    while stack:
        postorder.append(stack.pop())

    print(''.join(postorder))


solution(input().rstrip())
