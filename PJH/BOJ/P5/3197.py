from sys import stdin
from collections import deque

input = stdin.readline
directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def meet_swan(swan, next_swan, target, R, C, lake, swan_visited):
    global directions
    while swan:
        y, x = swan.popleft()

        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if (ny, nx) == target:
                return True


            if 0 <= ny < R and 0 <= nx < C and not swan_visited[ny][nx]:
                if lake[ny][nx] == '.':
                    swan.append((ny, nx))
                elif lake[ny][nx] == 'X':
                    next_swan.append((ny, nx))
                swan_visited[ny][nx] = True

    return False


def melt(water, next_water, R, C, lake, water_visited):
    global directions

    while water:
        y, x = water.popleft()
        lake[y][x] = '.'

        for dy, dx in directions:
            ny, nx = y + dy, x + dx

            if 0 <= ny < R and 0 <= nx < C and not water_visited[ny][nx]:
                if lake[ny][nx] == '.':
                    water.append((ny, nx))
                elif lake[ny][nx] == 'X':
                    next_water.append((ny, nx))
                water_visited[ny][nx] = True


def solution():
    R, C = map(int, input().split())
    lake = [list(input().rstrip()) for _ in range(R)]
    swan_visited = [[False for _ in range(C)] for _ in range(R)]
    water_visited = [[False for _ in range(C)] for _ in range(R)]

    swan = deque()
    next_swan = deque()
    water = deque()
    next_water = deque()
    target = ()
    for y in range(R):
        for x in range(C):
            if lake[y][x] == '.':
                water.append((y, x))
                water_visited[y][x] = True
            elif lake[y][x] == 'L':
                water.append((y, x))
                water_visited[y][x] = True
                if not swan:
                    swan.append((y, x))
                    swan_visited[y][x] = True
                else:
                    target = (y, x)
    answer = 0
    while True:
        melt(water, next_water, R, C, lake, water_visited)

        if meet_swan(swan, next_swan, target, R, C, lake, swan_visited):
            break



        water = next_water
        swan = next_swan
        next_water = deque()
        next_swan = deque()

        answer += 1

    print(answer)
solution()
