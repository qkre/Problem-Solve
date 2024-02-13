answer = 99999999


def dfs(board, ways, visited, x, y, w, h, itemX, itemY, count, path):
    global answer
    if x == itemX and y == itemY:
        answer = min(answer, count)
        return

    dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

    for i in range(4):
        nx, ny = dx[i] + x, dy[i] + y

        # 범위 내의 존재하고, 외곽선이 존재하며 방문 하지 않은 경우
        if (0 <= nx <= w and 0 <= ny <= h) and not visited[ny][nx] and board[ny][nx] == 1:
            # 길이 존재하는 경우
            if ways[y][x][i] == 1:
                visited[ny][nx] = True
                path.append((nx, ny))
                dfs(board, ways, visited, nx, ny, w, h, itemX, itemY, count + 1, path)
                path.pop()
                visited[ny][nx] = False


def solution(rectangle, characterX, characterY, itemX, itemY):
    global answer
    w, h = 0, 0

    for rect in rectangle:
        x1, y1, x2, y2 = rect
        w = max(w, x1, x2)
        h = max(h, y1, y2)

    board = [[0 for _ in range(w + 2)] for _ in range(h + 2)]
    ways = [[[0, 0, 0, 0] for _ in range(w + 2)] for _ in range(h + 2)]
    visited = [[False for _ in range(w + 2)] for _ in range(h + 2)]
    for rect in rectangle:
        x1, y1, x2, y2 = rect

        for y in range(y1, y2 + 1):
            if y == y1 or y == y2:
                for x in range(x1, x2 + 1):
                    board[y][x] = 1
            else:
                board[y][x1] = 1
                board[y][x2] = 1

        for y in range(y1, y2 + 1):
            for x in range(x1, x2 + 1):
                u, d, l, r = board[y - 1][x], board[y + 1][x], board[y][x - 1], board[y][x + 1]
                ways[y][x] = [u, d, l, r]

    for rect in rectangle:
        x1, y1, x2, y2 = rect

        for y in range(y1 + 1, y2):
            for x in range(x1 + 1, x2):
                board[y][x] = 0
                ways[y][x] = [0, 0, 0, 0]
                ways[y - 1][x][1] = 0
                ways[y + 1][x][0] = 0
                ways[y][x - 1][3] = 0
                ways[y][x + 1][2] = 0

    for _ in board:
        print(*_)

    print("==================")

    # 2사분면
    for y in range(0, h // 2 + 1):
        for x in range(0, w // 2):
            if ways[y][x].count(1) > 2:
                if ways[y + 1][x].count(1) > 2:
                    ways[y][x][1] = 0
                    ways[y + 1][x][0] = 0
                    board[y + 1][x] = 0
                if ways[y][x + 1].count(1) > 2:
                    ways[y][x][3] = 0
                    ways[y][x + 1][2] = 0
                    board[y][x + 1] = 0
    # 1사분면
    for y in range(0, h // 2 + 1):
        for x in range(w // 2 + 1, w + 1):
            if ways[y][x].count(1) > 2:
                if ways[y + 1][x].count(1) > 2:
                    ways[y][x][1] = 0
                    ways[y + 1][x][0] = 0
                    board[y + 1][x] = 0
                if ways[y][x - 1].count(1) > 2:
                    ways[y][x][2] = 0
                    ways[y][x - 1][3] = 0
                    board[y][x - 1] = 0

    # 3사분면
    for y in range(h // 2 + 1, h + 1):
        for x in range(0, w // 2 + 1):
            if ways[y][x].count(1) > 2:
                if ways[y - 1][x].count(1) > 2:
                    ways[y][x][0] = 0
                    ways[y - 1][x][1] = 0
                    board[y - 1][x] = 0
                if ways[y][x + 1].count(1) > 2:
                    ways[y][x][3] = 0
                    ways[y][x + 1][2] = 0
                    board[y][x + 1] = 0

    # 4사분면
    for y in range(h // 2 + 1, h + 1):
        for x in range(w // 2 + 1, w + 1):
            if ways[y][x].count(1) > 2:
                if ways[y - 1][x].count(1) > 2:
                    ways[y][x][0] = 0
                    ways[y - 1][x][1] = 0
                    board[y - 1][x] = 0
                if ways[y][x - 1].count(1) > 2:
                    ways[y][x][2] = 0
                    ways[y][x - 1][3] = 0
                    board[y][x - 1] = 0

    for _ in board:
        print(*_)

    for _ in ways:
        print(*_)

    visited[characterY][characterX] = True
    dfs(board, ways, visited, characterX, characterY, w, h, itemX, itemY, 0, [(characterX, characterY)])

    return answer


print(solution([[2, 2, 5, 5], [1, 3, 6, 4], [3, 1, 4, 6]], 1, 4, 6, 3))
