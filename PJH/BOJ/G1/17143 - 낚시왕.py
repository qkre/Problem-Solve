from sys import stdin

input = stdin.readline

class Shark:

    def __init__(self, r, c, s, d, z):
        self.row = r
        self.col = c
        self.speed = s
        self.direction = d
        self.size = z

def catch_shark(fisher, maps, R):
    for r in range(1, R + 1):
        if maps[r][fisher] != 0:
            catch = maps[r][fisher].size
            maps[r][fisher] = 0
            return catch
    return 0


def shark_move(maps, R, C):
    sharks = []
    row_tables = [i for i in range(R+1)] + [i for i in range(R - 1, 1, -1)]
    col_tables = [i for i in range(C+1)] + [i for i in range(C - 1, 1, -1)]
    for row in range(1, R + 1):
        for col in range(1, C + 1):
            if maps[row][col] != 0:
                sharks.append(maps[row][col])
                maps[row][col] = 0

    while sharks:
        shark = sharks.pop()
        row, col, speed, direction, size = shark.row, shark.col, shark.speed, shark.direction, shark.size

        if direction == 1:
            row = row_tables[(row - speed) % (R * 2 - 2)]
            if row > R:
                direction = 2
        elif direction == 2:
            row = row_tables[(row + speed) % (R * 2 - 2)]
            if row <= R:
                direction = 1
        elif direction == 3:
            col = col_tables[(col + speed) % (C * 2 - 2)]
            if col > C:
                direction = 4
        elif direction == 4:
            col = col_tables[(col - speed) % (C * 2 - 2)]
            if col <= C:
                direction = 3

        if maps[row][col] != 0:
            if maps[row][col].size < size:
                maps[row][col] = Shark(row, col, speed, direction, size)
        else:
            maps[row][col] = Shark(row, col, speed, direction, size)



def solution():
    R, C, M = map(int, input().split())

    maps = [[0 for _ in range(C + 1)] for _ in range(R + 1)]

    for _ in range(M):
        r, c, s, d, z = map(int, input().split())
        maps[r][c] = Shark(r, c, s, d, z)
    catch = 0

    for fisher in range(1, C + 1):
        catch += catch_shark(fisher, maps, R)
        shark_move(maps, R, C)

    return catch


print(solution())
