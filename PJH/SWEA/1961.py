import os
import sys
import copy

current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"input/{current_file}_input.txt", "r")
result = []

T = int(input())


def rotate(y, x, target, arr):
    global N

    if N - y - x == 1:
        return target

    for _ in range(N - y - x - 1):
        # right
        for i in range(x, N - x):
            if i == x:
                target[y][i] = arr[y + 1][i]
            else:
                target[y][i] = arr[y][i - 1]

        # down
        for i in range(y + 1, N - y):
            target[i][N - x - 1] = arr[i - 1][N - x - 1]

        # left
        for i in range(N - x - 1, x, -1):
            target[N - y - 1][i - 1] = arr[N - y - 1][i]

        # up
        for i in range(N - y - 1, y, -1):
            target[i - 1][x] = arr[i][x]

        arr = copy.deepcopy(target)

    return target


for case in range(1, T + 1):
    N = int(input())

    arr = list(list(map(int, input().split())) for _ in range(N))

    result.append(f"#{case}")

    rotate_result = []
    rotate_1 = []
    rotate_2 = []
    rotate_3 = []

    for i in range(N // 2):
        rotate_1 = rotate(i, i, arr, copy.deepcopy(arr))

    rotate_2 = copy.deepcopy(rotate_1)
    for i in range(N // 2):
        rotate_2 = rotate(i, i, rotate_2, copy.deepcopy(rotate_1))

    rotate_3 = copy.deepcopy(rotate_2)
    for i in range(N // 2):
        rotate_3 = rotate(i, i, rotate_3, copy.deepcopy(rotate_2))

    for i, j, k in zip(rotate_1, rotate_2, rotate_3):
        st = "".join(map(str, i))
        st += " "
        st += "".join(map(str, j))
        st += " "
        st += "".join(map(str, k))

        result.append(st)

for _ in result:
    print(_)

output = open(f"output/{current_file}_output.txt", "r").readlines()
output = [line.strip() for line in output]
print(result == output)
