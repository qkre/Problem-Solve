import os
import sys
from check_answer import check_answer

current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"../input/{current_file}.txt", "r", encoding="utf-8-sig")

from collections import deque, defaultdict

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder(node):
    global ans
    if node.left:
        inorder(tree[node.left])

    ans += node.data

    if node.right:
        inorder(tree[node.right])



result = []
for case in range(1, 10 + 1):
    ans = ""
    N = int(input())
    tree = defaultdict(Node)

    for _ in range(N):
        arr = list(input().split())
        tree[int(arr[0])] = Node(arr[1])

        if len(arr) > 2:
            tree[int(arr[0])].left = int(arr[2])
            if len(arr) > 3:
                tree[int(arr[0])].right = int(arr[3])


    inorder(tree[1])

    result.append(f"#{case} {ans}")

for r in result:
    print(r)

check_answer(current_file, result)
