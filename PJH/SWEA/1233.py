import os
import sys
from check_answer import check_answer

current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"../input/{current_file}.txt", "r", encoding="utf-8-sig")

from collections import deque, defaultdict

result = []


def move(x):

    moves = 0
    y = 0
    while

for case in range(1, 10 + 1):
    ans = 1
    N = int(input())

    maps = list(list(map(int, input().split())) for _ in range(100))

    for i in range(100):
        if maps[0][i]:


    result.append(f"#{case} {ans}")

for r in result:
    print(r)

check_answer(current_file, result)
