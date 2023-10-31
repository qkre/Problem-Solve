import os
import sys


current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"input/{current_file}_input.txt", "r")


result = []

T = int(input())


def shoot(direction, y, x):
    global H, W
    # 위
    if direction == 0:
        for i in range(y - 1, -1, -1):
            if arr[i][x] == ".":
                continue
            elif arr[i][x] == "*":
                arr[i][x] = "."
                break
            elif arr[i][x] == "#":
                break

    # 아래
    if direction == 1:
        for i in range(y + 1, H):
            if arr[i][x] == ".":
                continue
            elif arr[i][x] == "*":
                arr[i][x] = "."
                break
            elif arr[i][x] == "#":
                break

    # 왼쪽
    if direction == 2:
        for i in range(x - 1, -1, -1):
            if arr[y][i] == ".":
                continue
            elif arr[y][i] == "*":
                arr[y][i] = "."
                break
            elif arr[y][i] == "#":
                break

    # 오른쪽
    if direction == 3:
        for i in range(x + 1, W):
            if arr[y][i] == "*":
                arr[y][i] = "."
                break
            elif arr[y][i] == "#":
                break


def move(target):
    global H, W, direction, y, x
    if target == "U":
        if y > 0 and arr[y - 1][x] == ".":
            arr[y][x] = "."
            y -= 1
        arr[y][x] = "^"
        direction = 0
        return

    elif target == "D":
        if y < H - 1 and arr[y + 1][x] == ".":
            arr[y][x] = "."
            y += 1
        arr[y][x] = "v"
        direction = 1
        return

    elif target == "L":
        if x > 0 and arr[y][x - 1] == ".":
            arr[y][x] = "."
            x -= 1
        arr[y][x] = "<"
        direction = 2
        return

    elif target == "R":
        if x < W - 1 and arr[y][x + 1] == ".":
            arr[y][x] = "."
            x += 1
        arr[y][x] = ">"
        direction = 3
        return


for case in range(1, T + 1):
    H, W = map(int, input().split())

    arr = list(list(input()) for _ in range(H))

    N = int(input())
    commands = list(input())

    direction = 0
    x, y = 0, 0
    for i in range(H):
        for j in range(W):
            if arr[i][j] == "^":
                direction = 0
                x, y = j, i
                break
            elif arr[i][j] == "v":
                direction = 1
                x, y = j, i
                break
            elif arr[i][j] == "<":
                direction = 2
                x, y = j, i
                break
            elif arr[i][j] == ">":
                direction = 3
                x, y = j, i
                break

    for cmd in commands:
        if cmd == "S":
            shoot(direction, y, x)
        else:
            move(cmd)

    for i in range(H):
        if i == 0:
            result.append(f"#{case} {''.join(arr[i])}")
        else:
            result.append(f"{''.join(arr[i])}")


for _ in result:
    print(_)


output = open(f"input/{current_file}_output.txt", "r").readlines()
output = [line.strip() for line in output]

print("------------------- 오답 ------------------ ( 이 아래로 출력이 없으면 정답)")

for r, o in zip(result, output):
    if r != o:
        print(f"정답 : {o},     오답 : {r}")
