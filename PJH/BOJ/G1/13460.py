from sys import stdin
from collections import deque
from copy import deepcopy

input = stdin.readline


def bfs(board, N, M, red, blue, hole):
    visited = [[0 for _ in range(M)] for _ in range(N)]
    visited[red[0]][red[1]] = 1
    q = deque()
    path = []
    q.append([0, red, blue, board.copy()])

    while q:
        cost, rd, bd, board = q.popleft()
        if bd == (0, 0):
            continue
        if rd == (0, 0):
            return cost

        moves = move_list(board, rd[0], rd[1], bd[0], bd[1], N, M)

        for i in range(len(moves)):
            nrd, nbd, next_board, d = moves[i][0][0], moves[i][0][1], moves[i][1], moves[i][2]
            q.append([cost + 1, nrd, nbd, next_board])
    return -1

def is_loop(path, next_dir):
    if path[-1] == 'U' and next_dir == 'D':
        return True
    if path[-1] == 'D' and next_dir == 'U':
        return True
    if path[-1] == 'L' and next_dir == 'R':
        return True
    if path[-1] == 'R' and next_dir == 'L':
        return True
    return False


def move(board, sy, sx, N, M, D):
    moved = False
    # 상
    if D == 'U':
        for y in range(sy, 0, -1):
            if board[y][sx] == 'R' or board[y][sx] == 'B':
                if board[y - 1][sx] == 'O':
                    board[y][sx] = '.'
                    moved = True
                elif board[y - 1][sx] == '.':
                    board[y - 1][sx] = board[y][sx]
                    board[y][sx] = '.'
                    moved = True

    # 하
    if D == 'D':
        for y in range(sy, N - 1):
            if board[y][sx] == 'R' or board[y][sx] == 'B':
                if board[y + 1][sx] == 'O':
                    board[y][sx] = '.'
                elif board[y + 1][sx] == '.':
                    board[y + 1][sx] = board[y][sx]
                    board[y][sx] = '.'
    # 좌
    if D == 'L':
        for x in range(sx, 0, -1):
            if board[sy][x] == 'R' or board[sy][x] == 'B':
                if board[sy][x - 1] == 'O':
                    board[sy][x] = '.'
                elif board[sy][x - 1] == '.':
                    board[sy][x - 1] = board[sy][x]
                    board[sy][x] = '.'

    if D == 'R':
        for x in range(sx, M - 1):
            if board[sy][x] == 'R' or board[sy][x] == 'B':
                if board[sy][x + 1] == 'O':
                    board[sy][x] = '.'
                elif board[sy][x + 1] == '.':
                    board[sy][x + 1] = board[sy][x]
                    board[sy][x] = '.'

    return board


def find_ball(board, N, M):
    red = (0, 0)
    blue = (0, 0)
    for y in range(N):
        for x in range(M):
            if board[y][x] == 'R':
                red = (y, x)
            if board[y][x] == 'B':
                blue = (y, x)

    return [red, blue]


def is_moved(board, next_board):
    return True

    # for i, j in zip(board, next_board):
    #     if i != j:
    #         return True
    # return True


def move_list(board, ry, rx, by, bx, N, M):
    dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
    moves = []
    # 상하 서로 붙어 있는 경우
    if rx == bx:
        # 상
        if by < ry:
            # 빨간공 먼저 움직이기
            next_board = move(deepcopy(board), ry, rx, N, M, 'U')
            next_board = move(next_board, by, bx, N, M, 'U')
            if is_moved(board, next_board):
                moves.append([find_ball(next_board, N, M), next_board, 'U'])
        elif ry < by:
            next_board = move(deepcopy(board), by, bx, N, M, 'U')
            next_board = move(next_board, ry, rx, N, M, 'U')
            if is_moved(board, next_board):
                moves.append([find_ball(next_board, N, M), next_board, 'U'])

    if rx == bx:
        # 하
        if ry < by:
            next_board = move(deepcopy(board), ry, rx, N, M, 'D')
            next_board = move(next_board, by, bx, N, M, 'D')
            if is_moved(board, next_board):
                moves.append([find_ball(next_board, N, M), next_board, 'D'])

        elif by < ry:
            next_board = move(deepcopy(board), by, bx, N, M, 'D')
            next_board = move(next_board, ry, rx, N, M, 'D')
            if is_moved(board, next_board):
                moves.append([find_ball(next_board, N, M), next_board, 'D'])

        # 좌우
        for i in range(2, 4):
            D = "UDLR"[i]
            next_board = move(deepcopy(board), ry, rx, N, M, D)
            next_board = move(next_board, by, bx, N, M, D)
            if is_moved(board, next_board):
                moves.append([find_ball(next_board, N, M), next_board, D])

    # 좌우 서로 붙어 있는 경우
    if ry == by:
        # 좌
        if rx < bx:
            # 빨간공 먼저 움직이기
            next_board = move(deepcopy(board), ry, rx, N, M, 'L')
            next_board = move(next_board, by, bx, N, M, 'L')
            if is_moved(board, next_board):
                moves.append([find_ball(next_board, N, M), next_board, 'L'])
        elif bx < rx:
            next_board = move(deepcopy(board), by, bx, N, M, 'L')
            next_board = move(next_board, ry, rx, N, M, 'L')
            if is_moved(board, next_board):
                moves.append([find_ball(next_board, N, M), next_board, 'L'])

    if ry == by:
        # 우
        if bx < rx:
            next_board = move(deepcopy(board), ry, rx, N, M, 'R')
            next_board = move(next_board, by, bx, N, M, 'R')
            if is_moved(board, next_board):
                moves.append([find_ball(next_board, N, M), next_board, 'R'])

        elif rx < bx:
            next_board = move(deepcopy(board), by, bx, N, M, 'R')
            next_board = move(next_board, ry, rx, N, M, 'R')
            if is_moved(board, next_board):
                moves.append([find_ball(next_board, N, M), next_board, 'R'])

        # 상하
        for i in range(2):
            D = "UDLR"[i]
            next_board = move(deepcopy(board), ry, rx, N, M, D)
            next_board = move(next_board, by, bx, N, M, D)
            if is_moved(board, next_board):
                moves.append([find_ball(next_board, N, M), next_board, D])

    else:
        for i in range(4):
            D = "UDLR"[i]
            next_board = move(deepcopy(board), ry, rx, N, M, D)
            next_board = move(next_board, by, bx, N, M, D)
            if is_moved(board, next_board):
                moves.append([find_ball(next_board, N, M), next_board, D])

    return moves


def solution():
    N, M = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(N)]

    red, blue, hole = [], [], []
    for y in range(N):
        for x in range(M):
            if board[y][x] == 'R':
                red = (y, x)
            if board[y][x] == 'B':
                blue = (y, x)
            if board[y][x] == 'O':
                hole = (y, x)

    answer = bfs(board, N, M, red, blue, hole)
    print(answer)


solution()
