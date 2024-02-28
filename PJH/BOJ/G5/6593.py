from sys import stdin
from collections import deque

input = stdin.readline


def solution():
    d = [(0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1), (-1, 0, 0), (1, 0, 0)]
    while True:
        L, R, C = map(int, input().split())

        if L == R == C == 0:
            return

        buildings = []

        for i in range(L * 2):
            if i % 2 == 0:
                buildings.append([list(input().rstrip()) for _ in range(R)])
            else:
                input()

        S = ()
        E = ()
        visited = [[[False for _ in range(C)] for _ in range(R)] for _ in range(L)]

        for l in range(L):
            for r in range(R):
                for c in range(C):
                    if buildings[l][r][c] == 'S':
                        S = (l, r, c, 0)
                        visited[l][r][c] = True

                    elif buildings[l][r][c] == 'E':
                        E = (l, r, c)

        q = deque([S])
        escaped = False
        while q:
            l, r, c, count = q.popleft()

            if (l, r, c) == E:
                print(f"Escaped in {count} minute(s).")
                escaped = True
                break

            for dl, dr, dc in d:
                nl, nr, nc = l + dl, r + dr, c + dc

                if 0 <= nl < L and 0 <= nr < R and 0 <= nc < C and buildings[nl][nr][nc] != '#' and not visited[nl][nr][nc]:
                    q.append((nl, nr, nc, count+1))
                    visited[nl][nr][nc] = True

        if not escaped:
            print("Trapped!")

solution()
