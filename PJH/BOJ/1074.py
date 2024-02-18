cnt = -1


def solution(N, r, c):
    global cnt
    draw(N, 0, 0, r, c)


def draw(N, sx, sy, r, c):
    global cnt
    now = 2 ** (N-1)
    if N == 1:
        for i in range(2):
            for j in range(2):
                cnt += 1
                if i == r and j == c:
                    print(cnt)
                    quit()
        return

    if 0 <= c < 2 ** (N - 1):
        if 0 <= r < 2 ** (N - 1):
            # 2사분면
            cnt += 0
            draw(N - 1, 0, 0, r, c)

        else:
            # 3사분면
            cnt += now**2 * 2
            draw(N - 1, 0, 2 ** (N - 1), r-now, c)

    else:
        if 0 <= r < 2 ** (N - 1):
            # 1사분면
            cnt += now**2
            draw(N - 1, 2 ** (N - 1), 0, r, c-now)

        else:
            # 4사분면
            cnt += now**2 * 3
            draw(N - 1, 2 ** (N - 1), 2 ** (N - 1), r-now, c-now)



N, r, c = map(int, input().split())
solution(N, r, c)
