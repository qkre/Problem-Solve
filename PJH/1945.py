import os
import sys


current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"input/{current_file}_input.txt", "r")


result = []

T = int(input())

for case in range(1, T + 1):
    N = int(input())
    ans = [2, 3, 5, 7, 11]
    index = 0
    for i in ans:
        cnt = 0
        while N % i == 0:
            cnt += 1
            N = N // i

        ans[index] = cnt
        index += 1

    result.append(f"#{case} {' '.join(map(str, ans))}")

for _ in result:
    print(_)


output = open(f"input/{current_file}_output.txt", "r").readlines()
output = [line.strip() for line in output]

print("------------------- 오답 ------------------ ( 이 아래로 출력이 없으면 정답)")

for r, o in zip(result, output):
    if r != o:
        print(f"정답 : {o},     오답 : {r}")
