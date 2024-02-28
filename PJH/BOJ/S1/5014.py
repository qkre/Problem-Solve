from heapq import heappop, heappush
def solution():
    F, S, G, U, D = map(int, input().split())
    visited = [False] * (F+1)
    visited[S] = True
    q = [(0, S)]

    printed = False
    while q:
        count, floor = heappop(q)

        if floor == G:
            printed = True
            print(count)
            break

        for i in [U, -D]:
            new_floor = floor + i

            if 1 <= new_floor <= F and not visited[new_floor]:
                visited[new_floor] = True
                heappush(q, (count + 1, new_floor))

    if not printed:
        print("use the stairs")

solution()