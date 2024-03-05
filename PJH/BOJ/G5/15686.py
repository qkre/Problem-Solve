from sys import stdin
import itertools
from collections import deque

input = stdin.readline

def solution():
    answer = 0

    N, M = map(int, input().split())

    maps = list(list(map(int, input().split())) for _ in range(N))

    houses = []
    chickens = []
    for r in range(N):
        for c in range(N):
            if maps[r][c] == 1:
                houses.append((r, c))
            elif maps[r][c] == 2:
                chickens.append((r, c))


    nearest = []

    for house in houses:
        min_distance = (-1, float('inf'))

        for i in range(len(chickens)):

            distance = abs(house[0] - chickens[i][0]) + abs(house[1] - chickens[i][1])

            if distance < min_distance[1]:
                min_distance = (chickens[i], distance)

        nearest.append(min_distance[0])

    nearest = list(set(nearest))
    if len(nearest) > M:
        answer = float('inf')
        combs = list(itertools.combinations(chickens, M))

        for comb in combs:
            distances = [float('inf')] * len(houses)

            for i in range(len(houses)):
                house = houses[i]
                for chicken in comb:
                    distance = abs(house[0] - chicken[0]) + abs(house[1] - chicken[1])

                    if distance < distances[i]:
                        distances[i] = distance

            answer = min(sum(distances), answer)

    else:
        for house in houses:
            min_distance = float('inf')

            for chicken in nearest:
                distance = abs(house[0] - chicken[0]) + abs(house[1] - chicken[1])

                if distance < min_distance:
                    min_distance = distance
            answer += min_distance

    return answer
print(solution())

