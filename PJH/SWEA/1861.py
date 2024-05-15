import os
import sys

current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"../../input/{current_file}_input.txt", "r", encoding="utf-8-sig")

from collections import deque, defaultdict
result = []
T = int(input())

def bfs(x, y):
    cnt = 1

    q = deque([(x, y)])

    while q:
        cx, cy = q.popleft()

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = cx + dx, cy + dy

            if 0 <= nx < N and 0 <= ny < N and maps[cy][cx] + 1 == maps[ny][nx]:
                cnt += 1
                checked[ny][nx] = True
                q.append((nx, ny))

    return cnt

for case in range(1, T + 1):
    ans = 10e9
    max_cnt = 0
    N = int(input())
    maps = list(list(map(int, input().split())) for _ in range(N))
    checked = [[False for _ in range(N)] for _ in range(N)]
    for y in range(N):
        for x in range(N):
            if not checked[y][x]:
                checked[y][x] = True
                cnt = bfs(x, y)
                if max_cnt < cnt:
                    max_cnt = cnt
                    ans = maps[y][x]
                elif max_cnt == cnt:
                    ans = min(ans, maps[y][x])


    result.append(f"#{case} {ans} {max_cnt}")
for _ in result:
    print(_)

output = open(f"../../input/{current_file}_output.txt", "r").readlines()
output = [line.strip() for line in output]

print("------------------- 오답 ------------------ ( 이 아래로 출력이 없으면 정답)")

for y, o in zip(result, output):
    if y != o:
        print(f"정답 : {o},     오답 : {y}")
