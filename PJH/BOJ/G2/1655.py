from sys import stdin
from heapq import heappush, heappop

input = stdin.readline

def solution(N):
    max_heap = []
    min_heap = []

    for i in range(1, N+1):
        num = int(input())

        if i == 1:
            heappush(max_heap, -num)
        elif i == 2:
            heappush(min_heap, num)
        else:
            if i % 2 == 1:
                heappush(max_heap, -num)
            else:
                heappush(min_heap, num)


        if i > 1:
            if -max_heap[0] > min_heap[0]:
                temp = heappop(min_heap)
                heappush(min_heap, -heappop(max_heap))
                heappush(max_heap, -temp)

        print(-max_heap[0])


solution(int(input()))