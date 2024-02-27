from sys import stdin
from collections import deque
input = stdin.readline

def solution(N):
    arr = list(tuple(map(int, input().split())) for _ in range(N))
    arr.sort(key=lambda x:(x[0], -x[1]))
    arr = deque(arr)
    answer = 0
    S, E = 0, 0
    while arr:
        if (S, E) == (0, 0):
            S, E = arr.popleft()
            answer += E-S
        else:
            ns, ne = arr.popleft()
            if E <= ns:
                answer += ne-ns
                S, E = ns, ne

            elif ns < E <= ne:
                answer -= E - ns
                answer += ne - ns
                S, E = ns, ne

    return answer

print(solution(int(input())))