import os
import sys


current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"input/{current_file}_input.txt", "r")


result = []

T = int(input())

for case in range(1, T + 1):
    N = int(input())

    checked = [False] * 10

    K = 0
    while False in checked:
        K += 1
        now = list(map(int, list(str(N * K))))

        for _ in now:
            if not checked[_]:
                checked[_] = True

    result.append(f"#{case} {K*N}")

for _ in result:
    print(_)


output = open(f"input/{current_file}_output.txt", "r").readlines()
output = [line.strip() for line in output]

print("------------------- 오답 ------------------ ( 이 아래로 출력이 없으면 정답)")

for r, o in zip(result, output):
    if r != o:
        print(f"정답 : {o},     오답 : {r}")
