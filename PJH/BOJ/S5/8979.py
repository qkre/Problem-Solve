from collections import deque

def solution():
    N, K = map(int, input().split())
    nations = []
    for _ in range(N):
        n, g, s, b = map(int, input().split())

        nations.append([n, g, s, b])

    nations.sort(key= lambda x: (-x[1], -x[2], -x[3]))
    nations = deque(nations)

    rank = 1

    ranks = [[] for _ in range(N+1)]

    while nations:
        now = nations.popleft()
        ranks[rank].append(now)
        while True and nations:
            if now[1:] == nations[0][1:]:
                ranks[rank].append(nations.popleft())
            else:
                break

        rank += len(ranks[rank])

    for i in range(1, N+1):
        for nation in ranks[i]:
            if nation[0] == K:
                print(i)
                return


solution()