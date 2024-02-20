from sys import stdin

input = stdin.readline

T = int(input())
data = [list(map(int, input().split())) for _ in range(T)]


def solution(T, data):
    for M, N, x, y in data:
        target = [x, y]

        cnt = 1
        X, Y = 1, 1
        while True:
            state = False
            if X == x or Y == y:
                now = [X, Y]
                while True:
                    if now == target:
                        print(cnt)
                        break
                    if now == [M, N]:
                        print(-1)
                        break
                    now[0] += 1
                    now[1] += 1

                    if now[0] > M:
                        now[0] = 1
                    if now[1] > N:
                        now[1] = 1
                    cnt += 1


                break


            if M - X < N - Y:
                state = True

            if state:
                Y += (M-X)+1
                cnt += (M-X)+1
                X = 1

            else:
                cnt += (N-Y)+1
                X += (N-Y)+1
                Y = 1



solution(T, data)
