import os
import sys


current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"input/{current_file}_input.txt", "r", encoding="utf-8-sig")


result = []

T = int(input())

for case in range(1, T + 1):
    A, B = map(list, input().split())

    max_len = 0
    cnt = 0
    for i in range(len(A)):
        if not A[i] in B:
            continue

        cnt = 1

        t_2 = B[B.index(A[i]) :]

        for j in range(i + 1, len(A)):
            t_1 = A[j]
            if not t_1 in t_2:
                continue
            t_2 = t_2[t_2.index(A[j]) :]

            cnt += 1

        max_len = max(max_len, cnt)

    result.append(f"#{case} {max_len}")

for _ in result:
    print(_)


output = open(f"input/{current_file}_output.txt", "r").readlines()
output = [line.strip() for line in output]

print("------------------- 오답 ------------------ ( 이 아래로 출력이 없으면 정답)")

for r, o in zip(result, output):
    if r != o:
        print(f"정답 : {o},     오답 : {r}")
