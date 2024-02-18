import os
import sys


current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"input/{current_file}_input.txt", "r")


result = []

T = int(input())


def is_increasing(N):
    N = list(str(N))

    for i in range(len(N) - 1):
        if int(N[i]) > int(N[i + 1]):
            return False
    return True


for case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    ans = -1
    for i in range(N):
        for j in range(i + 1, N):
            if is_increasing(arr[i] * arr[j]):
                ans = max(ans, arr[i] * arr[j])

    result.append(f"#{case} {ans}")

for _ in result:
    print(_)


output = open(f"input/{current_file}_output.txt", "r").readlines()
output = [line.strip() for line in output]

print("------------------- 오답 ------------------ ( 이 아래로 출력이 없으면 정답)")

for r, o in zip(result, output):
    if r != o:
        print(f"정답 : {o},     오답 : {r}")
