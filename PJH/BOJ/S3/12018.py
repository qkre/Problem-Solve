from sys import stdin

input = stdin.readline


def solution():
    N, M = map(int, input().split())
    P = [0] * N
    for _ in range(N):
        Pi, Li = map(int, input().split())
        mileage = sorted(list(map(int, input().split())), reverse=True)
        if Pi < Li:
            P[_] = 1
        else:
            P[_] = min(mileage[:Li])


    P.sort()

    while sum(P) > M:
        P.pop()

    print(len(P))


solution()
