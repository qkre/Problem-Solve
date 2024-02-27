from sys import stdin
from collections import deque
from heapq import heappop, heappush

input = stdin.readline


def solution():
    N, M = map(int, input().split())

    count = 0

    arr = deque(list(map(int, input().split())))

    plugged = []
    while len(plugged) < N and arr:
        item = arr.popleft()
        if item not in plugged:
            plugged.append(item)

    while arr:
        max_heap = []

        item = arr.popleft()

        if item in plugged:
            continue

        any_pull = False
        will_pull = 0

        for now in plugged:
            if now in arr:
                heappush(max_heap, (-arr.index(now), now))

            else:
                will_pull = now
                any_pull = True
                break

        if any_pull:
            plugged.remove(will_pull)
            plugged.append(item)

        else:
            pull_item = heappop(max_heap)
            plugged.remove(pull_item[1])
            plugged.append(item)

        count += 1

    return count


print(solution())
