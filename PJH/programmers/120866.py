def solution(board):
    safe_area = [[True for _ in range(len(board[0]))] for _ in range(len(board))]

    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] == 1:
                dy, dx = [-1, -1, -1, 0, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 0, 1, -1, 0, 1]

                for i in range(9):
                    ny, nx = y + dy[i], x + dx[i]

                    if 0 <= ny < len(board) and 0 <= nx < len(board[0]) and safe_area[ny][nx]:
                        safe_area[ny][nx] = False

    answer = 0

    for row in safe_area:
        answer += row.count(True)

    return answer


print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]))
