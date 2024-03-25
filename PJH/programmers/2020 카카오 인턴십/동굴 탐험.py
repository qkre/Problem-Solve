from collections import deque, defaultdict

def solution(n, path, order):
    answer = True

    visited = [False] * n
    prev_visited = defaultdict(int)
    graph = defaultdict(list)
    for s, e in path:
        graph[s].append(e)
        graph[e].append(s)

    for p, n in order:
        prev_visited[n] = p


    q = deque()
    q.append((0, 0))
    visited[0] = True
    while q:
        moved, node = q.popleft()

        if moved > n * len(order):
            continue

        for next_node in graph[node]:
            if prev_visited[next_node]:
                if not visited[next_node]:
                    continue

            visited[next_node] = True
            q.append((moved+1, next_node))

    if False in visited:
        answer = False

    print(answer)

    return answer

solution(9,	[[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]],	[[8,5],[6,7],[4,1]])