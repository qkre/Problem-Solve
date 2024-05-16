from collections import deque

N, M = map(int, input().split())
R, C, D = map(int, input().split())
maps = list(list(map(int, input().split())) for _ in range(N))

direction = {
    0: (-1, 0),
    1: (0, 1),
    2: (1, 0),
    3: (0, -1)
}

q = deque([(R, C, D)])
count = 0
def is_dirty(r, c):

    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc

        if (0 <= nr < N and 0 <= nc < M) and maps[nr][nc] == 0:
            return True

    return False

while q:
    r, c, d = q.popleft()

    if maps[r][c] == 0:
        count += 1
        maps[r][c] = "C"

    if not is_dirty(r, c):
        if d == 0:
            rd = 2
        elif d == 1:
            rd = 3
        elif d == 2:
            rd = 0
        else:
            rd = 1

        dr, dc = direction[rd]

        if 0 <= r + dr < N and 0 <= c + dc < M and maps[r + dr][c + dc] != 1:
            q.append((r + dr, c + dc, d))
            continue
        break
    else:
        while True:
            d = (d - 1) % 4
            dr, dc = direction[d]
            nr, nc = r + dr, c + dc
            if( 0 <= nr < N and 0 <= nc < M )and maps[nr][nc] == 0:
                q.append((nr, nc, d))
                break

print(count)