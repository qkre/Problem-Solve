from sys import stdin
from collections import defaultdict, deque
from heapq import heappop, heappush

input = stdin.readline


def solution():
    T = int(input())

    for _ in range(T):
        N, K = map(int, input().split())

        D = [0] + list(map(int, input().split()))

        graph = [[] for _ in range(N + 1)]
        post_graph = [[] for _ in range(N + 1)]

        for i in range(K):
            s, e = map(int, input().split())

            graph[s].append(e)
            post_graph[e].append(s)

        W = int(input())

        NEED = [False] * (N + 1)

        q = deque([W])

        while q:
            node = q.popleft()
            NEED[node] = True

            for prev in post_graph[node]:
                if not NEED[prev]:
                    q.append(prev)

        heap = []

        for i in range(1, N + 1):
            if not post_graph[i]:
                heappush(heap, [D[i], i])

        answer = 0
        while heap:
            cost, node = heappop(heap)
            answer += cost

            for i in range(len(heap)):
                heap[i][0] -= cost
                if heap[i][0] < 0:
                    heap[i][0] = 0

            for next_node in graph[node]:
                post_graph[next_node].remove(node)
                if not post_graph[next_node] and NEED[next_node]:
                    heappush(heap, [D[next_node], next_node])

        print(answer)


solution()
