from sys import stdin
from collections import deque

input = stdin.readline

head, tail = [0, 0], [0, 0, 'R']
changed = []


def tail_move():
    global changed, head, tail

    if changed:
        if changed[0][:2] == tail[:2]:
            tail[2] = changed[0][2]
            changed.pop(0)

    if tail[2] == 'R':
        tail[1] += 1
    elif tail[2] == 'L':
        tail[1] -= 1
    elif tail[2] == 'U':
        tail[0] -= 1
    elif tail[2] == 'D':
        tail[0] += 1


def move_right(maps, N):
    global head, tail

    if head[1] + 1 < N:
        if maps[head[0]][head[1] + 1] == 2:
            return False

        if maps[head[0]][head[1] + 1] != 1:
            maps[tail[0]][tail[1]] = 0
            tail_move()

        maps[head[0]][head[1] + 1] = 2
        head[1] += 1

        return True

    return False


def move_left(maps, N):
    global head, tail

    if head[1] - 1 >= 0:
        if maps[head[0]][head[1] - 1] == 2:
            return False

        if maps[head[0]][head[1] - 1] != 1:
            maps[tail[0]][tail[1]] = 0
            tail_move()

        maps[head[0]][head[1] - 1] = 2
        head[1] -= 1
        return True
    return False


def move_up(maps, N):
    global head, tail

    if head[0] - 1 >= 0:
        if maps[head[0] - 1][head[1]] == 2:
            return False

        if maps[head[0] - 1][head[1]] != 1:
            maps[tail[0]][tail[1]] = 0
            tail_move()

        maps[head[0] - 1][head[1]] = 2
        head[0] -= 1

        return True
    return False


def move_down(maps, N):
    global head, tail

    if head[0] + 1 < N:
        if maps[head[0] + 1][head[1]] == 2:
            return False

        if maps[head[0] + 1][head[1]] != 1:
            maps[tail[0]][tail[1]] = 0
            tail_move()

        maps[head[0] + 1][head[1]] = 2
        head[0] += 1

        return True
    return False


def solution():
    global changed, head, tail
    N = int(input())
    K = int(input())
    apples = list(tuple(map(int, input().split())) for _ in range(K))
    L = int(input())
    commands = []

    for _ in range(L):
        X, C = input().split()
        commands.append((int(X), C))

    maps = [[0 for _ in range(N)] for _ in range(N)]

    for r, c in apples:
        maps[r - 1][c - 1] = 1

    maps[0][0] = 2
    D = 'R'
    answer = 0
    game_over = False
    while not game_over:
        if commands:
            times, command = commands.pop(0)

            while answer < times:
                answer += 1

                if D == 'L':
                    if not move_left(maps, N):
                        print(answer)
                        game_over = True
                        break
                elif D == 'R':
                    if not move_right(maps, N):
                        print(answer)
                        game_over = True
                        break
                elif D == 'U':
                    if not move_up(maps, N):
                        print(answer)
                        game_over = True
                        break
                elif D == 'D':
                    if not move_down(maps, N):
                        print(answer)
                        game_over = True
                        break

            if command == 'L':
                if D == 'U':
                    D = 'L'
                elif D == 'D':
                    D = 'R'
                elif D == 'R':
                    D = 'U'
                elif D == 'L':
                    D = 'D'

            if command == 'D':
                if D == 'U':
                    D = 'R'
                elif D == 'D':
                    D = 'L'
                elif D == 'R':
                    D = 'D'
                elif D == 'L':
                    D = 'U'

            changed.append([head[0], head[1], D])

        else:
            answer += 1

            if D == 'L':
                if not move_left(maps, N):
                    print(answer)
                    game_over = True
                    break
            elif D == 'R':
                if not move_right(maps, N):
                    print(answer)
                    game_over = True
                    break
            elif D == 'U':
                if not move_up(maps, N):
                    print(answer)
                    game_over = True
                    break
            elif D == 'D':
                if not move_down(maps, N):
                    print(answer)
                    game_over = True
                    break


solution()
