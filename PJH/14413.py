import os
import sys


current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"input/{current_file}_input.txt", "r", encoding="utf-8-sig")


result = []

T = int(input())


def check_valid():
    global N, M

    start_y = -1
    start_x = -1
    if "#" in arr[0]:
        start_x = arr[0].index("#")
        start_y = 0
    elif "." in arr[0]:
        start_x = arr[0].index(".")
        start_y = 0
    else:
        for i in range(1, N):
            if "#" in arr[i]:
                start_x = arr[i].index("#")
                start_y = i
                break
            elif "." in arr[i]:
                start_x = arr[i].index(".")
                start_y = i
                break

    if start_x == -1 or start_y == -1:
        return True

    char = arr[start_y][start_x]

    if abs(start_x - start_y) % 2 == 0:
        for y in range(N):
            if y % 2 == 0:
                for x in range(0, M, 2):
                    if arr[y][x] != "?" and arr[y][x] != char:
                        return False
                for x in range(1, M, 2):
                    if arr[y][x] == char:
                        return False
            else:
                for x in range(1, M, 2):
                    if arr[y][x] != "?" and arr[y][x] != char:
                        return False
                for x in range(0, M, 2):
                    if arr[y][x] == char:
                        return False
    else:
        for y in range(N):
            if y % 2 == 0:
                for x in range(1, M, 2):
                    if arr[y][x] != "?" and arr[y][x] != char:
                        return False
                for x in range(0, M, 2):
                    if arr[y][x] == char:
                        return False
            else:
                for x in range(0, M, 2):
                    if arr[y][x] != "?" and arr[y][x] != char:
                        return False
                for x in range(1, M, 2):
                    if arr[y][x] == char:
                        return False

    return True


for case in range(1, T + 1):
    N, M = map(int, input().split())

    arr = list(list(input()) for _ in range(N))

    P = check_valid()

    if P:
        result.append(f"#{case} possible")
    else:
        result.append(f"#{case} impossible")


for _ in result:
    print(_)


output = open(f"input/{current_file}_output.txt", "r").readlines()
output = [line.strip() for line in output]

print("------------------- 오답 ------------------ ( 이 아래로 출력이 없으면 정답)")

for r, o in zip(result, output):
    if r != o:
        print(f"정답 : {o},     오답 : {r}")
