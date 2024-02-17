import math
def solution(n,a,b):

    if b < a:
        a, b = b, a

    while n > 1:
        mid = n // 2

        if a <= mid < b:
            for i in range(1, 20):
                if 2**i == n:
                    return i

        n //= 2
        if a > n:
            a -= n
            b -= n


print(solution(16, 8, 9))