import os
import sys


current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"input/{current_file}_input.txt", "r")


result = []

T = int(input())

def fp(N, p):
    global C
    if p == 0:
        return 1

    half = fp(N, p // 2)

    if p % 2 == 0:
        return (half % C) ** 2 % C
    else:
        return (((half * N) % C) * (half % C)) % C


C = 1234567891

fac = [1] * 1000001

for i in range(1, 1000001):
    fac[i] = (fac[i - 1] * i) % C

for case in range(1, T + 1):
    N, R = map(int, input().split())

    # [ (N! % C) / { ((N-R)! % C) * (R! % C) } ] % C
    # => [ (N! %C) * { ((N-R)! % C) * (R! % C) }** (C-2) ] % C

    top = fac[N] % C
    bottom = (fac[N - R] % C) * (fac[R] % C)
    bottom_reversed = fp(bottom, C - 2)

    ans = top * bottom_reversed % C

    result.append(f"#{case} {ans}")

for _ in result:
    print(_)


output = open(f"input/{current_file}_output.txt", "r").readlines()
output = [line.strip() for line in output]

print("------------------- 오답 ------------------ ( 이 아래로 출력이 없으면 정답)")

for r, o in zip(result, output):
    if r != o:
        print(f"정답 : {o},     오답 : {r}")
