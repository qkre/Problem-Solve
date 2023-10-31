import os
import sys
import copy

current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"input/{current_file}_input.txt", "r")


result = []

T = int(input())

for case in range(1, T + 1):
    N = list(input())

    min_value = int("".join(N))
    max_value = int("".join(N))

    for i in range(len(N) - 1):
        for j in range(i + 1, len(N)):
            temp = copy.deepcopy(N)
            t = temp[i]
            temp[i] = temp[j]
            temp[j] = t

            if len(str(int("".join(temp)))) == len(N):
                min_value = min(min_value, int("".join(temp)))
                max_value = max(max_value, int("".join(temp)))

    result.append(f"#{case} {min_value} {max_value}")

for _ in result:
    print(_)


output = open(f"input/{current_file}_output.txt", "r").readlines()
output = [line.strip() for line in output]

print("------------------- 오답 ------------------ ( 이 아래로 출력이 없으면 정답)")

for r, o in zip(result, output):
    if r != o:
        print(f"정답 : {o},     오답 : {r}")
