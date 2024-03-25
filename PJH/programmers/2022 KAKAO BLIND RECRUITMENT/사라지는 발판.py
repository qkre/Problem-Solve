EMPTY = 0
AVAILABLE = 1
def solution(board, aloc, bloc):
    answer = 0
    result, count = play(board, aloc[0], aloc[1], bloc[0], bloc[1])
    answer = count

    print(answer)
    return answer


def play(board, r1, c1, r2, c2):
    N, M = len(board), len(board[0])
    if board[r1][c1] == EMPTY:
        return False, 0

    board[r1][c1] = EMPTY

    max_lose = 0
    min_win = float('inf')

    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r1 + dr, c1 + dc

        if 0 <= nr < N and 0 <= nc < M and board[nr][nc] == AVAILABLE:
            result, count = play(board, r2, c2, nr, nc)

            if not result:
                max_lose = max(max_lose, count + 1)
            else:
                min_win = min(min_win, count + 1)

    board[r1][c1] = AVAILABLE

    if min_win < float('inf'):
        return True, min_win
    else:
        return False, max_lose

solution([[1, 1, 1], [1, 1, 1], [1, 1, 1]], [1, 0], [1, 2])
solution([[1, 1, 1], [1, 0, 1], [1, 1, 1]], [1, 0], [1, 2])
solution([[1, 1, 1, 1, 1]], [0, 0], [0, 4])
