from sys import stdin
from heapq import heappop, heappush
input = stdin.readline

def solution():
    N = int(input())
    lessons = [tuple(map(int, input().split())) for _ in range(N)]
    lessons.sort()

    room = []
    heappush(room, lessons[0][1])

    for i in range(1, N):
        if room[0] > lessons[i][0]:
            heappush(room, lessons[i][1])
        else:
            heappop(room)
            heappush(room, lessons[i][1])

    print(len(room))

solution()