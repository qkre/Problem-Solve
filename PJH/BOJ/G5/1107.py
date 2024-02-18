def solution(N, M, broken):
    cnt = abs(N-100)
    buttons = []

    for i in range(10):
        if i not in broken:
            buttons.append(i)

    if N == 100:
        return 0

    if not buttons:
        return abs(100 - N)

    for i in range(1000001):
        num_list = list(map(int,str(i)))
        valid = True
        for n in num_list:
            if n in broken:
                valid = False
                break

        if valid:
            cnt = min(cnt, len(num_list) + abs(N - i))

    return cnt

import sys
lines = sys.stdin.readlines()
N, M, broken = 0, 0, []
for i in range(len(lines)):
    if i == 0:
        N = int(lines[i])
    if i == 1:
        M = int(lines[i])
    if i == 2:
        broken = list(map(int,lines[i].split()))

print(solution(N, M, broken))