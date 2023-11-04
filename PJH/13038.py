import os
import sys


current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"input/{current_file}_input.txt", "r", encoding="utf-8-sig")


result = []

T = int(input())

def operation(index):
    global N
    cnt = 0
    date = 0
    while cnt != N:
        date += 1

        if class_date[index] == 1:
            cnt += 1
            if cnt == N:
                break

        index += 1

        if index == 7:
            index = 0
    
    return date

for case in range(1, T + 1):
    N = int(input())

    class_date = list(map(int, input().split()))
    date = 0
    cnt = 0
    min_date = 100000000

    # M
    index = 0
    min_date = min(operation(index), min_date)
    # T
    index = 1
    min_date = min(operation(index), min_date)

    # W
    index = 2
    min_date = min(operation(index), min_date)

    # T
    index = 3
    min_date = min(operation(index), min_date)

    # F
    index = 4
    min_date = min(operation(index), min_date)

    # S
    index = 5
    min_date = min(operation(index), min_date)

    # S
    index = 6
    min_date = min(operation(index), min_date)



    result.append(f"#{case} {min_date}")

for _ in result:
    print(_)


output = open(f"input/{current_file}_output.txt", "r").readlines()
output = [line.strip() for line in output]

print("------------------- 오답 ------------------ ( 이 아래로 출력이 없으면 정답)")

for r, o in zip(result, output):
    if r != o:
        print(f"정답 : {o},     오답 : {r}")
