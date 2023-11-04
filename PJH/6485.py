import os
import sys


current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"input/{current_file}_input.txt", "r", encoding="utf-8-sig")


result = []

T = int(input())

for case in range(1, T + 1):
    N = int(input())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    P = int(input())
    C = []
    for _ in range(P):
        C.append(int(input()))

    ans = []
    for c in C:
        cnt = 0
        for i in range(N):
            if A[i] <= c <= B[i]:
                cnt += 1

        ans.append(cnt)

    result.append(f"#{case} {' '.join(list(map(str, ans)))}")

for _ in result:
    print(_)


output = open(f"input/{current_file}_output.txt", "r").readlines()
output = [line.strip() for line in output]

print("------------------- 오답 ------------------ ( 이 아래로 출력이 없으면 정답)")

for r, o in zip(result, output):
    if r != o:
        print(f"정답 : {o},     오답 : {r}")
