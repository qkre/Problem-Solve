from sys import stdin
from collections import Counter

input = stdin.readline

N = int(input())


def find(A, root):
    if A == root[A]:
        return A
    else:
        root[A] = find(root[A], root)
        return root[A]


def union(A, B, root):
    A = find(A, root)
    B = find(B, root)
    if A < B:
        root[B] = A
    else:
        root[A] = B


def CCW(P1, P2, P3):
    x1, y1 = P1
    x2, y2 = P2
    x3, y3 = P3

    S = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)

    if S > 0:
        return 1
    elif S < 0:
        return -1
    else:
        return 0


points = []
root = [i for i in range(N)]

for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())

    points.append([(x1, y1), (x2, y2)])

for i in range(N):
    A, B = points[i]
    for j in range(N):
        if i == j:
            continue
        cross = False
        C, D = points[j]

        ABC = CCW(A, B, C)
        ABD = CCW(A, B, D)
        CDA = CCW(C, D, A)
        CDB = CCW(C, D, B)

        if ABC * ABD <= 0 and CDA * CDB <= 0:
            if ABC * ABD == 0 and CDA * CDB == 0:
                if A > B:
                    temp = B
                    B = A
                    A = temp
                if C > D:
                    temp = C
                    C = D
                    D = temp

                if C <= B and A <= D:
                    cross = True
            else:
                cross = True

        if cross:
            union(i, j, root)

for i in range(N):
    root[i] = find(i, root)

counter = Counter(root)
print(len(counter))
print(counter.most_common()[0][1])