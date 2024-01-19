def solution(maps):
    map = [list(i) for i in maps]
    len_X = len(map[0])
    len_Y = len(map)
    answer = []

    day = 0

    visited = [[False] * len_X for _ in range(len_Y)]

    def move(x, y,):
        nonlocal day

        day += int(map[y][x])
        dy, dx = [-1, 0, 1, 0], [0, -1, 0, 1]

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]

            if 0 <= ny < len_Y and 0 <= nx < len_X and map[ny][nx] != "X" and not visited[ny][nx]:
                visited[ny][nx] = True
                move(nx, ny)



    for y in range(len_Y):
        for x in range(len_X):
            if map[y][x] != "X" and not visited[y][x]:
                day = 0
                visited[y][x] = True
                move(x, y)
                answer.append(day)

    answer.sort()
    if len(answer) == 0:
        answer.append(-1)

    print(answer)
    return answer

solution(["X591X","X1X5X","X231X", "1XXX1"])