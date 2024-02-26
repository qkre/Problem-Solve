from sys import stdin
input = stdin.readline

def solution():
    R, C = map(int, input().split())
    maps = [list(input().rstrip()) for _ in range(R)]
    count = 0
    rank = 1
    checked = [False] * R
    ranks = [0] * 10
    idx = C-2
    while count < 9:
        ranked = False
        for i in range(R):
            if maps[i][idx] != '.' and not checked[int(maps[i][idx])]:
                ranks[int(maps[i][idx])] = rank
                checked[int(maps[i][idx])] = True
                ranked = True
                count += 1

        if ranked:
            rank += 1

        idx -= 1

    for i in range(1, 10):
        print(ranks[i])

solution()
