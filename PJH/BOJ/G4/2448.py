N = int(input())

maps = [[' ' for _ in range(N * 2)] for _ in range(N)]


def patterns(n, x, y, is_blank, maps, status, cnt):
    if is_blank:
        return

    if n == 3:

        for i in range(y, y + 3):
            for j in range(x, x + 5):
                if i == y and j == x + 2:
                    maps[i][j] = '*'
                elif i == y + 1 and (j == x + 1 or j == x + 3):
                    maps[i][j] = '*'
                elif i == y + 2:
                    maps[i][j] = '*'
        return

    if cnt == N // 3:
        for i in range(6):
            status[i] = not status[i]

        cnt = 0

    patterns(n // 2, x, y, status[0], maps, status, cnt + 1)
    patterns(n // 2, x + n // 2, y, status[1], maps, status, cnt + 1)
    patterns(n // 2, x + n, y, status[2], maps, status, cnt + 1)

    patterns(n // 2, x, y + n // 2, status[3], maps, status, cnt + 1)
    patterns(n // 2, x + n // 2, y + n // 2, status[4], maps, status, cnt + 1)
    patterns(n // 2, x + n, y + n // 2, status[5], maps, status, cnt + 1)


patterns(N, 0, 0, False, maps, [True, False, True, False, True, False], 0)

for _ in maps:
    print(''.join(_))
