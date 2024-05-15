import os
import sys
from check_answer import check_answer

current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"../input/{current_file}.txt", "r", encoding="utf-8-sig")

from heapq import heappush, heappop

def find(value):
    if parents[value] != value:
        parents[value] = find(parents[value])
    return parents[value]
def union(A, B):
    A = find(A)
    B = find(B)

    if A < B:
        parents[B] = A
    else:
        parents[A] = B

result = []
T = int(input())
for case in range(1, T + 1):
    ans = 0

    N = int(input())

    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))

    E = float(input())

    pq = []

    for i in range(N):
        for j in range(i + 1, N):
            heappush(pq, (E * ((abs(X[i] - X[j]) ** 2 + abs(Y[i] - Y[j]) ** 2) ** 0.5) ** 2, i, j))

    parents = [i for i in range(N)]


    while pq:
        cost, start, end = heappop(pq)

        if parents.count(0) == N:
            break

        if find(start) != find(end):
            ans += cost
            union(start, end)




    result.append(f"#{case} {round(ans)}")

for r in result:
    print(r)

check_answer(current_file, result)
