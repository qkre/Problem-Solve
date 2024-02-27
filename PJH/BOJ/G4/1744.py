from sys import stdin
from heapq import heappop, heappush
input = stdin.readline


def solution(N):
    answer = 0

    min_heap = []
    max_heap = []

    for _ in range(N):
        i = int(input())
        if i > 0:
            heappush(max_heap, -i)
        else:
            heappush(min_heap, i)

    min_v = False
    max_v = False


    while min_heap:
        S = heappop(min_heap)

        if not min_heap:
            min_v = S
            break

        E = heappop(min_heap)

        answer += S * E

    while max_heap:
        S = -heappop(max_heap)

        if not max_heap:
            max_v = S
            break

        E = -heappop(max_heap)

        if S == 1 or E == 1:
            answer += S + E
        else:
            answer += S * E

    if min_v:
        if max_v:
            answer += min_v + max_v
        else:
            answer += min_v
    else:
        if max_v:
            answer += max_v



    return answer


print(solution(int(input())))
