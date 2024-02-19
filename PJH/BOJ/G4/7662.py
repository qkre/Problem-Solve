from heapq import heappop, heappush, heapify
from sys import stdin

input = stdin.readline


def solution():
    T = int(input())

    for _ in range(T):
        k = int(input())

        min_heap = []
        max_heap = []
        visited = [0] * k

        for i in range(k):
            cmd, num = input().split()
            num = int(num)
            if cmd == 'I':
                heappush(min_heap, (num, i))
                heappush(max_heap, (-1 * num, i))

            if cmd == 'D':
                if num == -1:
                    if min_heap:
                        visited[heappop(min_heap)[1]] = 1
                else:
                    if max_heap:
                        visited[heappop(max_heap)[1]] = 1

            while max_heap and visited[max_heap[0][1]] == 1:
                heappop(max_heap)

            while min_heap and visited[min_heap[0][1]] == 1:
                heappop(min_heap)

        if min_heap and max_heap:
            print(-1 * heappop(max_heap)[0], heappop(min_heap)[0])
        else:
            print("EMPTY")


solution()
