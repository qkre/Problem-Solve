import os
import sys
from test import check_answer

current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"../../input/{current_file}_input.txt", "r", encoding="utf-8-sig")

result = []
T = int(input())


def is_palindrome(s):
    if s == s[::-1]:
        return True

    return False


for case in range(1, T + 1):
    S = list(input())
    N = len(S)
    ans = is_palindrome(S) and is_palindrome(S[:(N - 1) // 2]) and is_palindrome(S[(N - 1) // 2 + 1:])

    if ans:
        result.append(f"#{case} YES")
    else:
        result.append(f"#{case} NO")


for _ in result:
    print(_)

check_answer(current_file, result)
