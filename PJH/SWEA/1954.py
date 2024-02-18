import sys

sys.stdin = open("input/1954_input.txt", "r")

T = int(input())


def move(x, y, depth, direction):
    global N, snail_map

    if depth == N**2 + 1:
        return

    snail_map[y][x] = depth

    # right
    if direction == 0:
        if x < N - 1 and snail_map[y][x + 1] == 0:
            move(x + 1, y, depth + 1, 0)
        else:
            move(x, y + 1, depth + 1, 1)

    # down
    if direction == 1:
        if y < N - 1 and snail_map[y + 1][x] == 0:
            move(x, y + 1, depth + 1, 1)
        else:
            move(x - 1, y, depth + 1, 2)

    # left
    if direction == 2:
        if x > 0 and snail_map[y][x - 1] == 0:
            move(x - 1, y, depth + 1, 2)
        else:
            move(x, y - 1, depth + 1, 3)

    # up
    if direction == 3:
        if y > 0 and snail_map[y - 1][x] == 0:
            move(x, y - 1, depth + 1, 3)
        else:
            move(x + 1, y, depth + 1, 0)


for case in range(1, T + 1):
    global N
    N = int(input())

    snail_map = list([0 for _ in range(N)] for _ in range(N))

    snail_map[0][0] = 1

    move(0, 0, 1, 0)

    print(f"#{case}")
    for row in snail_map:
        print(*row)
