from sys import stdin

input = stdin.readline


def solution(N):
    maps = [[1 for _ in range(N + 1)] for _ in range(N + 1)]

    for i in range(1, N + 1):
        temp = list(map(int, input().split()))
        for j in range(1, N + 1):
            maps[i][j] = temp[j - 1]

    dp = [[[0, 0, 0] for _ in range(N + 1)] for _ in range(N + 1)]

    dp[1][2][0] = 1

    for y in range(1, N + 1):
        for x in range(1, N + 1):

            if maps[y][x] == 1:
                continue

            for dy, dx in [(0, -1), (-1, 0), (-1, -1)]:

                py, px = y + dy, x + dx

                if maps[py][px] == 1:
                    continue

                # hor = 이전 hor, 이전 dia
                if (dy, dx) == (0, -1):
                    dp[y][x][0] += dp[py][px][0]
                    dp[y][x][0] += dp[py][px][2]
                elif (dy, dx) == (-1, 0):
                    dp[y][x][1] += dp[py][px][1]
                    dp[y][x][1] += dp[py][px][2]
                else:
                    if maps[y - 1][x] == 1 or maps[y][x - 1] == 1:
                        continue

                    dp[y][x][2] += dp[py][px][0]
                    dp[y][x][2] += dp[py][px][1]
                    dp[y][x][2] += dp[py][px][2]

    answer = sum(dp[N][N])

    return answer


print(solution(int(input())))
