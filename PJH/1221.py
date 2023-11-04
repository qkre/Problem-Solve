import os
import sys


current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"input/{current_file}_input.txt", "r", encoding="utf-8-sig")


seq = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

result = []

T = int(input())


for case in range(1, T + 1):
    input()

    s = list(input().split())
    A = []

    for i in range(10):
        A.append(f"{seq[i]} " * s.count(seq[i]))

    ans = ""
    for i in A:
        ans += i

    result.append(f"#{case}")
    result.append(f"{ans[:-1]}")


for _ in result:
    print(_)


output = open(f"input/{current_file}_output.txt", "r").readlines()
output = [line.strip() for line in output]

print("------------------- 오답 ------------------ ( 이 아래로 출력이 없으면 정답)")

for r, o in zip(result, output):
    if r != o:
        print(f"정답 : {o},     오답 : {r}")
        # print("오답")
