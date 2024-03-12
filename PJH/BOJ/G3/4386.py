from sys import stdin

input = stdin.readline

def find(root, v):
    if root[v] == v:
        return v
    else:
        root[v] = find(root, root[v])
        return root[v]

def union(root, a, b):
    a = find(root, a)
    b = find(root, b)

    if a < b:
        root[b] = a
    else:
        root[a] = b

def solution():
    N = int(input())

    stars = []
    root = [i for i in range(N+1)]

    for _ in range(N):
        stars.append(tuple(map(float, input().split())))

    edges = []

    for i in range(N):
        s1 = stars[i]
        for j in range(i + 1, N):
            s2 = stars[j]
            edges.append((i+1, j+1, ((s1[0] - s2[0]) ** 2 + (s1[1] - s2[1]) ** 2) ** 0.5))

    edges.sort(key=lambda x:x[2], reverse=True)

    cnt = 0
    answer = 0

    while cnt < N-1:
        S, E, C = edges.pop()

        if find(root, S) == find(root, E):
            continue

        union(root, S, E)
        cnt += 1
        answer += C


    print(round(answer, 2))

solution()