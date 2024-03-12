from sys import stdin

input = stdin.readline


def solution():
    N, K = map(int, input().split())

    table = [0] * (K + 1)

    for _ in range(N):
        w, v = map(int, input().split())

        if w > K:
            continue

        for i in range(K, 0, -1):
            if i + w <= K and table[i] != 0:
                table[i + w] = max(table[i + w], table[i] + v)
        table[w] = max(table[w], v)

    print(max(table))

solution()
