import os
import sys
import copy

current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"input/{current_file}_input.txt", "r")
result = []

T = int(input())

def dfs(s):
    global N, length

    length = max(length, visited.count(True))
    
    for i in graph[s]:
        if not visited[i]:
            visited[i] = True
            dfs(i)

            visited[i] = False

        

for case in range(1, T + 1):

    N, M = map(int, input().split())

    graph = [[] for _ in range(N)]
    visited = [False] * N
    length = 1

    for _ in range(M):
        S, E = map(int, input().split())
        graph[S-1].append(E-1)
        graph[E-1].append(S-1)
    
    if M > 0:
        for i in range(N):
            for j in graph[i]:
                visited[i] = True
                visited[j] = True
                dfs(j)
                visited[i] = False
                visited[j] = False

    result.append(f"#{case} {length}")
for _ in result:
    print(_)

output = open(f"input/{current_file}_output.txt", "r").readlines()
output = [line.strip() for line in output]
print(result == output)
