from sys import stdin
from heapq import heappop, heappush

input = stdin.readline


def find(root, v):
    if root[v] == v:
        return v
    else:
        root[v] = find(root, root[v])
        return root[v]


def union(root, A, B):
    A = find(root, A)
    B = find(root, B)

    if A < B:
        root[B] = A
    else:
        root[A] = B


def solution():
    N = int(input())
    root = [i for i in range(N + 1)]
    planets = [tuple(map(int, input().split())) for _ in range(N)]
    answer = 0
    X = []
    Y = []
    Z = []

    for i in range(N):
        X.append((planets[i][0], i + 1))
        Y.append((planets[i][1], i + 1))
        Z.append((planets[i][2], i + 1))

    X.sort()
    Y.sort()
    Z.sort()

    pq = []

    for i in range(N - 1):
        heappush(pq, (abs(X[i][0] - X[i + 1][0]), X[i][1], X[i + 1][1]))
        heappush(pq, (abs(Y[i][0] - Y[i + 1][0]), Y[i][1], Y[i + 1][1]))
        heappush(pq, (abs(Z[i][0] - Z[i + 1][0]), Z[i][1], Z[i + 1][1]))

    cnt = 0
    while cnt < N - 1:
        cost, S, E = heappop(pq)

        if find(root, S) == find(root, E):
            continue

        union(root, S, E)
        cnt += 1
        answer += cost

    print(answer)


solution()
