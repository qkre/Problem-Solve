import os
import sys
from check_answer import check_answer

current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"../input/{current_file}.txt", "r", encoding="utf-8-sig")

result = []
T = int(input())

def dfs(depth, current):
    global ans, N, length
    if depth == N:
        ans = max(ans, int(''.join(current)))
        return

    for i in range(length):
        for j in range(i+1, length):
            current[i], current[j] = current[j], current[i]
            if (''.join(current), depth) not in visited:
                visited.append((''.join(current), depth))
                dfs(depth+1, current)
            current[i], current[j] = current[j], current[i]

for case in range(1, T + 1):
    ans = 0

    numbers, N = map(int, input().split())
    numbers = list(str(numbers))
    length = len(numbers)
    visited = []

    dfs(0, numbers)


    result.append(f"#{case} {ans}")

for r in result:
    print(r)

check_answer(current_file, result)
