from sys import stdin

input = stdin.readline


def solution(N):
    arr = list(list(map(int, input().split())) for _ in range(N))

    max_f, max_s, max_t = arr[0][0], arr[0][1], arr[0][2]
    min_f, min_s, min_t = arr[0][0], arr[0][1], arr[0][2]


    for i in range(1, N):
        max_nf = max(max_f, max_s) + arr[i][0]
        max_ns = max(max_f, max_s, max_t) + arr[i][1]
        max_nt = max(max_s, max_t) + arr[i][2]

        min_nf = min(min_f, min_s) + arr[i][0]
        min_ns = min(min_f, min_s, min_t) + arr[i][1]
        min_nt = min(min_s, min_t) + arr[i][2]


        max_f = max_nf
        max_s = max_ns
        max_t = max_nt

        min_f = min_nf
        min_s = min_ns
        min_t = min_nt



    print(max(max_f, max_s, max_t), min(min_f, min_s, min_t))

solution(int(input()))
