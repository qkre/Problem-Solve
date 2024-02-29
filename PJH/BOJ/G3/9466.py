from sys import stdin
from collections import deque

input = stdin.readline

team = False
visited = []
def dfs(target, S, E, path, arr):
    global team, visited
    if target == E:
        # print(path)
        for s in path:
            visited[s-1] = True
        team = True
        return

    if E in path:
        team = False
        return

    path.append(E)
    dfs(target, E, arr[E-1], path, arr)

def solution(T):
    global team, visited
    for case in range(T):
        N = int(input())
        arr = list(map(int, input().split()))
        visited = [False] * N
        answer = 0
        for i in range(N):
            if not visited[i]:

                dfs(i+1, i+1, arr[i], [i+1], arr)

                if not team:
                    answer += 1

        print(answer)
solution(int(input()))