def solution(n, wires):
    answer = n - 2
    length = len(wires)
    wires.sort()

    for i in range(length):
        temp_wire = wires.copy()
        temp_wire.pop(i)
        tree = [[] for _ in range(n + 1)]

        for s, e in temp_wire:
            tree[s].append(e)
            tree[e].append(s)

        visited = [False for _ in range(n + 1)]

        main_branch = bfs(tree, visited)
        another_branch = n - main_branch

        answer = min(answer, abs(main_branch - another_branch))

    return answer


def bfs(tree, visited):
    cnt = 0

    from collections import deque
    q = []
    for branch in tree:
        if not branch:
            continue
        q = deque(branch)
        break

    while q:
        edge = q.popleft()
        visited[edge] = True
        cnt += 1
        for e in tree[edge]:
            if not visited[e]:
                q.append(e)

    return cnt


print(solution(8, [[1,2],[1,3],[1,4],[4,5],[5,6],[6,7],[6,8]]))
