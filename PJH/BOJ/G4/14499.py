from sys import stdin
from collections import deque

input = stdin.readline


class DICE:

    def __init__(self, x, y):
        self.X = x
        self.Y = y

        self.bottom = 0
        self.top = 0
        self.head = 0
        self.tail = 0
        self.left = 0
        self.right = 0

    def print_top(self, maps):
        if maps[self.Y][self.X] == 0:
            maps[self.Y][self.X] = self.bottom
        else:
            self.bottom = maps[self.Y][self.X]
            maps[self.Y][self.X] = 0
        print(self.top)

    def move_down(self, maps, N):
        if self.Y + 1 < N:
            self.Y += 1
            tmp = [self.bottom, self.tail, self.top, self.head]

            self.bottom = tmp[3]
            self.tail = tmp[0]
            self.top = tmp[1]
            self.head = tmp[2]

            self.print_top(maps)

    def move_up(self, maps):
        if self.Y - 1 >= 0:
            self.Y -= 1
            tmp = [self.bottom, self.tail, self.top, self.head]

            self.top = tmp[3]
            self.tail = tmp[2]
            self.bottom = tmp[1]
            self.head = tmp[0]

            self.print_top(maps)

    def move_left(self, maps):
        if self.X - 1 >= 0:
            self.X -= 1
            tmp = [self.bottom, self.right, self.top, self.left]

            self.bottom = tmp[3]
            self.right = tmp[0]
            self.top = tmp[1]
            self.left = tmp[2]

            self.print_top(maps)

    def move_right(self, maps, M):
        if self.X+1 < M:
            self.X += 1
            tmp = [self.bottom, self.right, self.top, self.left]

            self.bottom = tmp[1]
            self.right = tmp[2]
            self.top = tmp[3]
            self.left = tmp[0]

            self.print_top(maps)


def solution():
    N, M, x, y, K = map(int, input().split())

    maps = list(list(map(int, input().split())) for _ in range(N))

    dice = DICE(y, x)
    commands = deque(list(map(int, input().split())))

    while commands:
        c = commands.popleft()

        if c == 1:
            dice.move_right(maps, M)
        elif c == 2:
            dice.move_left(maps)
        elif c == 3:
            dice.move_up(maps)
        elif c == 4:
            dice.move_down(maps, N)


solution()
