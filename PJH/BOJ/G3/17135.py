from sys import stdin
import itertools
from copy import deepcopy
from collections import deque

input = stdin.readline


def attack(new_board, N, M, X, D):
    distance = D + 1
    target = (-1, -1)
    for y in range(N - 1, -1, -1):
        for x in range(M):
            if new_board[y][x] != 0 and (abs(N - y) + abs(X - x) < distance):
                distance = abs(N - y) + abs(X - x)
                target = (y, x)
    if target != (-1, -1):
        new_board[target[0]][target[1]] +=1


def count(new_board, N, M):
    cnt = 0

    for y in range(N):
        for x in range(M):
            if new_board[y][x] > 1:
                cnt += 1

    return cnt


def move(new_board, N, M):
    next_board = [[0 for _ in range(M)] for _ in range(N + 1)]
    for y in range(1, N + 1):
        if y == N:
            next_board[y] = new_board[y]
        else:
            for x in range(M):
                if new_board[y - 1][x] != 1:
                    next_board[y][x] = 0
                else:
                    next_board[y][x] = 1

    return next_board


def check(board, N, M):
    for y in range(N):
        for x in range(M):
            if board[y][x] == 1:
                return True

    return False


def solution():
    N, M, D = map(int, input().split())

    board = [list(map(int, input().split())) for _ in range(N)]

    combs = list(itertools.combinations([_ for _ in range(M)], 3))
    answer = 0
    for place in combs:
        new_board = deepcopy(board)
        new_answer = 0
        archers = [0] * M
        for archer in place:
            archers[archer] = 1

        new_board.append(archers)

        while check(new_board, N, M):
            # attack
            for x in range(M):
                if new_board[N][x] == 1:
                    attack(new_board, N, M, x, D)

            # count
            new_answer += count(new_board, N, M)

            # move
            new_board = move(new_board, N, M)

        answer = max(answer, new_answer)

    return answer


print(solution())
