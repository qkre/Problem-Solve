from sys import stdin
from collections import defaultdict, deque

input = stdin.readline


def bfs_eatable(N, shark, fishes, maps):
    distance = [[float('inf') for _ in range(N)] for _ in range(N)]
    distance[shark[0]][shark[1]] = 0

    q = deque([(shark[0], shark[1])])
    size = shark[2]
    while q:
        r, c = q.popleft()

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc

            if 0 <= nr < N and 0 <= nc < N and maps[nr][nc] <= size:
                if distance[r][c] + 1 < distance[nr][nc]:
                    distance[nr][nc] = distance[r][c] + 1
                    q.append((nr, nc))

    eatables = []
    for i in range(1, size):
        for fish in fishes[i]:
            eatables.append((distance[fish[0]][fish[1]], fish[0], fish[1], i))

    if not eatables:
        return False

    eatables.sort()
    if eatables[0][0] == float('inf'):
        return False

    fish_pos = tuple([eatables[0][1], eatables[0][2]])

    fishes[eatables[0][3]].remove(fish_pos)

    return fish_pos

def bfs_shark(N, shark, fish_pos, maps):
    distance = [[float('inf') for _ in range(N)] for _ in range(N)]
    distance[shark[0]][shark[1]] = 0

    q = deque([(shark[0], shark[1])])
    size = shark[2]
    while q:
        r, c = q.popleft()

        if (r, c) == fish_pos:
            break

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc

            if 0 <= nr < N and 0 <= nc < N and maps[nr][nc] <= size:
                if distance[r][c] + 1 < distance[nr][nc]:
                    distance[nr][nc] = distance[r][c] + 1
                    q.append((nr, nc))

    maps[shark[0]][shark[1]] = 0
    maps[fish_pos[0]][fish_pos[1]] = 9

    return distance[fish_pos[0]][fish_pos[1]]

def solution():
    N = int(input())

    maps = [list(map(int, input().split())) for _ in range(N)]
    fishes = defaultdict(list)
    shark = ()

    for r in range(N):
        for c in range(N):
            if maps[r][c] == 9:
                shark = (r, c, 2, 0)
            elif maps[r][c] != 0:
                fishes[maps[r][c]].append((r, c))

    answer = 0

    while True:
        fish_pos = bfs_eatable(N, shark, fishes, maps)
        if not fish_pos:
            break
        move_cnt = bfs_shark(N, shark, fish_pos, maps)



        if shark[3] + 1 == shark[2]:
            shark = (fish_pos[0], fish_pos[1], shark[2] + 1, 0)
        else:
            shark = (fish_pos[0], fish_pos[1], shark[2], shark[3] + 1)


        answer += move_cnt

    print(answer)


solution()
