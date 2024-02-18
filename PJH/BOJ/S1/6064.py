from sys import stdin

input = stdin.readline

T = int(input())
data = [list(map(int, input().split())) for _ in range(T)]


def solution(T, data):
    for M, N, x, y in data:
        target = [x, y]

        now = [0, 0]
        cnt = 0
        X, Y = 0, 0
        while True:
            cnt += 1
            X += 1
            Y += 1

            if X > M:
                X = 1
            if Y > N:
                Y = 1

            now = [X, Y]
            if now == target:
                print(cnt)
                break
            if now == [M, N]:
                print(-1)
                break


solution(T, data)
