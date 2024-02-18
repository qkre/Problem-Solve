import os
import sys


current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"input/{current_file}_input.txt", "r", encoding="utf-8-sig")


result = []

T = int(input())

for case in range(1, T + 1):
    arr = list(list(input()) for _ in range(8))

    valid = True
    rook = 0
    for row in arr:
        if row.count("O") > 1:
            valid = False
            break

    if valid:
        for x in range(8):
            cnt = 0
            for y in range(8):
                if arr[y][x] == "O":
                    cnt += 1
                    if cnt > 1:
                        valid = False
                        break

    if valid:
        for row in arr:
            rook += row.count("O")
        if rook != 8:
            valid = False

    if valid:
        result.append(f"#{case} yes")
    else:
        result.append(f"#{case} no")


for _ in result:
    print(_)


output = open(f"input/{current_file}_output.txt", "r").readlines()
output = [line.strip() for line in output]

print("------------------- 오답 ------------------ ( 이 아래로 출력이 없으면 정답)")

for r, o in zip(result, output):
    if r != o:
        print(f"정답 : {o},     오답 : {r}")
