answer = 0
visited = []

def solution(n, computers):
    global answer, visited

    visited = [False] * (n+1)


    def bfs(s):
        global answer, visited

        answer += 1

        q = []

        for i in range(n):
            if not visited[i+1] and computers[s-1][i] == 1:
                q.append(i+1)

        while q:
            s = q[0]
            visited[s] = True
            q = q[1:]

            for i in range(n):
                if not visited[i + 1] and computers[s-1][i] == 1:
                    q.append(i + 1)


    for i in range(1, n+1):
        if not visited[i]:
            visited[i] = True
            bfs(i)


    return answer

print(solution(3,	[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))