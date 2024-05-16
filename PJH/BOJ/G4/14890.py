N, L = map(int, input().split())
maps = list(list(map(int, input().split())) for _ in range(N))


def row_road(c):
    height = maps[0][c]
    down_hill, up_hill = False, False
    r = 0
    while r < N - 1:
        if r + L < N and height != maps[r + L][c]:
            # down_hill
            if maps[r + L][c] < height:
                for i in range(1, L + 1):
                    if maps[r + i][c] != maps[r + L][c]:
                        return False

                if maps[r + L][c] < height and not up_hill:
                    down_hill = True
                    height -= 1
                    r += L
                    continue
            # up_hill
            if maps[r + L][c] > height:
                for i in range(L):
                    if maps[r + i][c] != height:
                        return False

                if maps[r + L][c] > height and not down_hill:
                    up_hill = True
                    height += 1
                    r += L
                    continue

        if maps[r + 1][c] != height:
            return False
        r += 1
        down_hill = up_hill = False

    return True


def col_road(r):
    height = maps[r][0]
    down_hill, up_hill = False, False
    c = 0
    while c < N - 1:
        if c + L < N and height != maps[r][c + L]:

            # down_hill
            if maps[r][c + L] < height and not up_hill:
                for i in range(1, L + 1):
                    if maps[r][c + i] != maps[r][c + L]:
                        return False

                down_hill = True
                height -= 1
                c += L
                continue
            # up_hill
            if maps[r][c + L] > height and not down_hill:
                for i in range(L):
                    if maps[r][c + i] != height:
                        return False

                up_hill = True
                height += 1
                c += L
                continue

        if maps[r][c + 1] != height:
            return False
        c += 1
        down_hill = up_hill = False
    return True


roads = 0

for i in range(N):
    if row_road(i):
        roads += 1
    if col_road(i):
        roads += 1

print(roads)
