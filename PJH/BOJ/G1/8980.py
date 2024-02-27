from sys import stdin
from collections import deque
from heapq import heappop, heappush

input = stdin.readline


def solution():
    answer = 0
    N, C = map(int, input().split())
    M = int(input())

    boxes = list(tuple(map(int, input().split())) for _ in range(M))
    boxes.sort(key=lambda x: x[1])
    boxes = deque(boxes)

    capacities = [0] * (N + 1)

    towns = [0] * (N + 1)

    while boxes:
        start, finish, cost = boxes.popleft()

        cost = min(C - max(capacities[start: finish]), cost)

        for i in range(start, finish):
            capacities[i] += cost
            if capacities[i] > C:
                capacities[i] = C

        towns[finish] += cost


    return sum(towns)


print(solution())
