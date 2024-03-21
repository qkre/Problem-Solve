def solution():
    H, W, N, M = map(int, input().split())

    answer = 0

    for i in range(0, H, N+1):
        for j in range(0, W, M+1):
            answer += 1


    print(answer)
solution()