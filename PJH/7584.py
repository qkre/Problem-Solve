import os
import sys


current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"input/{current_file}_input.txt", "r", encoding="utf-8-sig")


result = []

T = int(input())


def f(arr):
    for i in range(len(arr)):
        if arr[i] == "0":
            arr[i] = "1"
        else:
            arr[i] = "0"

    return arr


def g(arr):
    return list(reversed(arr))


P = [["0"], ["001"]]



for case in range(1, T + 1):
    K = int(input())
    



for _ in result:
    print(_)


output = open(f"input/{current_file}_output.txt", "r").readlines()
output = [line.strip() for line in output]

print("------------------- 오답 ------------------ ( 이 아래로 출력이 없으면 정답)")

for r, o in zip(result, output):
    if r != o:
        print(f"정답 : {o},     오답 : {r}")
