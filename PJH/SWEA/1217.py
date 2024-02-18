import os
import sys


current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"input/{current_file}_input.txt", "r")


result = []

T = 10


def pow(N, p):
    if p == 0:
        return 1

    half = pow(N, p // 2)

    if p % 2 == 0:
        return half**2
    else:
        return half**2 * N


for case in range(1, T + 1):
    N = int(input())
    A, B = map(int, input().split())

    ans = pow(A, B)

    result.append(f"#{case} {ans}")


for _ in result:
    print(_)


output = open(f"input/{current_file}_output.txt", "r").readlines()
output = [line.strip() for line in output]

print("------------------- 오답 ------------------ ( 이 아래로 출력이 없으면 정답)")

for r, o in zip(result, output):
    if r != o:
        print(f"정답 : {o},     오답 : {r}")
