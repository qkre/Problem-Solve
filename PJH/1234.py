import os
import sys


current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"input/{current_file}_input.txt", "r")


result = []

T = 10


def double_check():
    global arr
    for i in range(len(arr) - 1):
        if arr[i] == arr[i + 1]:
            arr = arr[:i] + arr[i + 2 :]
            i = 0

    return False


for case in range(1, T + 1):
    N, arr = input().split()
    N = int(N)
    arr = list(arr)


    while True:
        for i in range(len(arr) - 1):
            if arr[i] == arr[i + 1]:
                arr[i] = "X"
                arr[i + 1] = "X"

        if not "X" in arr:
            break

        while "X" in arr:
            arr.remove("X")

    result.append(f"#{case} {''.join(arr)}")

for _ in result:
    print(_)


output = open(f"input/{current_file}_output.txt", "r").readlines()
output = [line.strip() for line in output]

print("------------------- 오답 ------------------ ( 이 아래로 출력이 없으면 정답)")

for r, o in zip(result, output):
    if r != o:
        print(f"정답 : {o},     오답 : {r}")
