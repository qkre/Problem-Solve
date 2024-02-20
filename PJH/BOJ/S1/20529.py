from sys import stdin
input = stdin.readline

def solution():
    T = int(input())
    for _ in range(T):
        N = int(input())
        arr = list(input().split())

        graph = [[0 for _ in range(N)] for _ in range(N)]

        for i in range(N):
            for j in range(i+1, N):

                for k in range(4):
                    if arr[i][k] != arr[j][k]:
                        graph[i][j] += 1
                        graph[j][i] += 1

        for i in range(N):
            for j in range(i+1, N):
                q = (i, j)

                visited = [False] * N
                visited[j] = True

                while q:
                    s, e = q.popleft()



solution()