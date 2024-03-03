N = int(input())

maps = [[' ' for _ in range(N)] for _ in range(N)]


def pattern(n, x, y, is_blank, maps):
    if is_blank:
        for i in range(y, y + 3):
            for j in range(x, x + 3):
                maps[i][j] = ' '

        return

    if n == 3:
        for i in range(y, y + 3):
            for j in range(x, x + 3):
                if i == y + 1 and j == x + 1:
                    maps[i][j] = ' '
                    continue
                maps[i][j] = '*'

        return



    pattern(n // 3, x, y, False, maps)
    pattern(n // 3, x + (n // 3), y, False, maps)
    pattern(n // 3, x + 2 * (n // 3), y, False, maps)

    pattern(n // 3, x, y + (n // 3), False, maps)
    pattern(n // 3, x + (n // 3), y + (n // 3), True, maps)
    pattern(n // 3, x + 2 * (n // 3), y + (n // 3), False, maps)

    pattern(n // 3, x, y + 2 * (n // 3), False, maps)
    pattern(n // 3, x + (n // 3), y + 2 * (n // 3), False, maps)
    pattern(n // 3, x + 2 * (n // 3), y + 2 * (n // 3), False, maps)

pattern(N, 0, 0, False, maps)

for _ in maps:
    print(''.join(_))