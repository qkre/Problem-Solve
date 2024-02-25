from sys import stdin

input = stdin.readline

def rotate(B, M, K):
    rotated = [[0 for _ in range(M)] for _ in range(K)]

    for y in range(K):
        for x in range(M):
            rotated[y][x] = B[y][x]

    return rotated

def solution():
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]

    M, K = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(M)]

    B = rotate(B, M, K)

    answer = [[0 for _ in range(N)] for _ in range(K)]

    for y in range(N):
        for x in range(K):
            for i in range(M):
                answer[y][x] += A[y][i] * B[y][i]

    print(answer)

solution()