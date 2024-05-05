import os
import sys
from test import check_answer

current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"../../input/{current_file}_input.txt", "r", encoding="utf-8-sig")

from math import gcd

result = []
T = int(input())

def lcm(n, m):
    return n // gcd(n, m) * m

for case in range(1, T + 1):
    N, M = map(int, input().split())
    S = list(input().split())
    T = list(input().split())

    common = []

    for i in range(lcm(N, M)):
        common.append(S[i % N] + T[i % M])


    Q = int(input())

    ans = []
    for _ in range(Q):
        Y = int(input())
        ans.append(common[Y % lcm(N, M) - 1])

    result.append(f"#{case} {' '.join(ans)}")

for _ in result:
    print(_)

check_answer(current_file, result)
