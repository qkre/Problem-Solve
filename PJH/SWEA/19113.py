import os
import sys
from test import check_answer

current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"../../input/{current_file}_input.txt", "r", encoding="utf-8-sig")

result = []
T = int(input())

def is_discount(n, p):
    if n % 4 != 0:
        return False
    if n // 4 * 3 not in p:
        return False

    return True

for case in range(1, T + 1):
    N = int(input())
    P = list(map(int, input().split()))

    ans = []
    checked = 0
    while checked < 2*N:
        n = P.pop()
        if is_discount(n, P):
            P.remove(n // 4 * 3)
            ans.append(n // 4 * 3)
            checked += 2
        else:
            checked += 1

    result.append(f"#{case} {' '.join(map(str, ans[::-1]))}")

for _ in result:
    print(_)

check_answer(current_file, result)
