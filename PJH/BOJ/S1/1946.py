from collections import deque
T = int(input())

for case in range(T):
    N = int(input())

    applicants = list(tuple(map(int, input().split())) for _ in range(N))
    applicants.sort()

    ans = 1
    minimum_rank = applicants[0][1]
    for i in range(1, N):
        if minimum_rank > applicants[i][1]:
            ans += 1
            minimum_rank = applicants[i][1]

    print(ans)