import os
import sys
from check_answer import check_answer

current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"../input/{current_file}.txt", "r", encoding="utf-8-sig")

from collections import deque, defaultdict

result = []

def post_order(node):
    if node:
        post_order(left[node])
        post_order(right[node])

        if tree[node] == "+":
            tree[node] = int(tree[left[node]]) + int(tree[right[node]])

        elif tree[node] == "-":
            tree[node] = int(tree[left[node]]) - int(tree[right[node]])

        if tree[node] == "*":
            tree[node] = int(tree[left[node]]) * int(tree[right[node]])

        if tree[node] == "/":
            tree[node] = int(tree[left[node]]) / int(tree[right[node]])

    return


for case in range(1, 10 + 1):
    ans = 0

    N = int(input())
    tree = [0] * (N + 1)
    left = [0] * (N + 1)
    right = [0] * (N + 1)

    for _ in range(N):
        S = input().split()
        tree[int(S[0])] = S[1]

        if len(S) == 4:
            left[int(S[0])] = int(S[2])
            right[int(S[0])] = int(S[3])

    post_order(1)
    result.append(f"#{case} {int(tree[1])}")
for r in result:
    print(r)

check_answer(current_file, result)
