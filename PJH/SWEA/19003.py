import os
import sys
from test import check_answer

current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"../../input/{current_file}_input.txt", "r", encoding="utf-8-sig")

result = []
T = int(input())

def is_palindrome(S):
    if S == S[::-1]:
        return True
    return False

for case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(input() for _ in range(N))

    pal = False

    comb = []

    for s in arr:
        if is_palindrome(s):
            pal = s
        elif ''.join(reversed(s)) in arr:
            comb.append(s)

    if pal:
        comb.append(pal)

    result.append(f"#{case} {len(comb) * M}")

for _ in result:
    print(_)

check_answer(current_file, result)
