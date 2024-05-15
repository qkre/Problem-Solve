import os
import sys
from check_answer import check_answer

current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"../input/{current_file}.txt", "r", encoding="utf-8-sig")

from collections import deque, defaultdict
from itertools import permutations

result = []
T = int(input())


def dfs(depth, perms, left, right):
    global N, ans, total

    if depth == N:
        ans += 1
        return

    if left > total // 2:
        n = N - depth
        ans += (2 ** n)
        return

    dfs(depth + 1, perms, left + perms[depth], right)
    if right + perms[depth] <= left:
        dfs(depth + 1, perms, left, right + perms[depth])

def permutation(depth, now):
    global N

    if depth == N:
        dfs(0, now, 0, 0)
        return


    for i in range(N):
        if not visited[i]:
            visited[i] = True
            now.append(arr[i])
            permutation(depth + 1, now)
            now.pop()
            visited[i] = False

for case in range(1, T + 1):
    ans = 0

    N = int(input())
    arr = list(map(int, input().split()))
    total = sum(arr)
    visited = [False] * N
    permutation(0, [])
    result.append(f"#{case} {ans}")

for r in result:
    print(r)

check_answer(current_file, result)
