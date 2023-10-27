import sys

sys.stdin = open("input/1215_input.txt", "r")
result = []


def check(direction, y, x):
    global N

    if direction == 0 and x + N <= 8:
        reversed_arr = list(reversed(arr[y][x : x + N]))
        if arr[y][x : x + N] == reversed_arr:
            return True

    elif direction == 1 and y + N <= 8:
        temp = []
        for i in range(N):
            temp.append(arr[y + i][x])

        if temp == list(reversed(temp)):
            return True

    return False


for case in range(1, 11):
    N = int(input())

    arr = list(list(input()) for _ in range(8))

    cnt = 0

    for i in range(8):
        for j in range(8):
            if check(0, i, j):
                cnt += 1
            if check(1, i, j):
                cnt += 1

    result.append(f"#{case} {cnt}")

for _ in result:
    print(_)

output = open("output/1215_output.txt", "r").readlines()
output = [line.strip() for line in output]
print(result == output)
