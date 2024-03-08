from sys import stdin
from collections import deque


input = stdin.readline


def solution():
    N, K = map(int, input().split())
    visited = [False] * 200001
    cost = [float('inf')] * 200001
    cost[N] = 0
    visited[N] = True

    q = deque([N])
    answer = 0
    if N != K:
        while q:
            C = q.popleft()

            if C == K:
                answer += 1

                while q:
                    C = q.popleft()
                    if C == K:
                        answer += 1

                break

            for n in (C-1, C+1, C*2):
                if 0<= n < 200001 and cost[C] + 1 <= cost[n]:
                    visited[n] = True
                    cost[n] = cost[C] + 1
                    q.append(n)
    else:
        answer = 1


    print(cost[K])
    print(answer)

solution()
