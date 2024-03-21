from collections import defaultdict, deque


def solution(edges):
    MAX_LEN = 1_000_001

    answer = [0, 0, 0, 0]

    go = [[] for _ in range(MAX_LEN)]
    take = [[] for _ in range(MAX_LEN)]

    for g, t in edges:
        go[g].append(t)
        take[t].append(g)

    start = 0

    for i in range(MAX_LEN):
        if len(go[i]) >= 2 and len(take[i]) == 0:
            start = i
            break

    answer = [start, 0, 0, 0]

    visited = [False] * MAX_LEN

    def bfs(i):
        q = deque([i])
        visited[i] = True

        while q:
            node = q.popleft()

            if not go[node]:
                answer[2] += 1
                return
            if len(go[node]) == 2 and len(take[node]) == 2:
                answer[3] += 1
                return
            for next_node in go[node]:
                if not visited[next_node]:
                    visited[next_node] = True
                    q.append(next_node)

        answer[1] += 1

    for node in go[start]:
        take[node].remove(start)
        bfs(node)

    print(answer)
    return answer


solution([[2, 3], [4, 3], [1, 1], [2, 1]])
