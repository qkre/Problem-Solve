import os
import sys


current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"input/{current_file}_input.txt", "r")


result = []

T = int(input())


def permutation(depth, perm):
    if depth == 3:
        if not sum(perm) in sum_list:
            sum_list.append(sum(perm))
        return

    for i in arr:
        if not i in perm:
            perm.append(i)
            permutation(depth + 1, perm)
            perm.pop()


for case in range(1, T + 1):
    arr = list(map(int, input().split()))

    sum_list = []

    for i in arr:
        permutation(1, [i])

    sum_list.sort(reverse=True)

    result.append(f"#{case} {sum_list[4]}")

for _ in result:
    print(_)


output = open(f"input/{current_file}_output.txt", "r").readlines()
output = [line.strip() for line in output]

print("------------------- 오답 ------------------ ( 이 아래로 출력이 없으면 정답)")

for r, o in zip(result, output):
    if r != o:
        print(f"정답 : {o},     오답 : {r}")
