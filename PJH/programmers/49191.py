from heapq import heappush, heappop


def solution(n, results):
    answer = 0
    results.sort()
    winners = [[] for _ in range(n + 1)]
    losers = [[] for _ in range(n + 1)]

    for winner, loser in results:
        winners[winner].append(loser)
        losers[loser].append(winner)

    print(winners)
    print(losers)

    q = []
    last = 1
    for i in range(1, n + 1):
        if winners[i]:
            q.append(winners[i][0])
            last = i

    visited = [False] * (n + 1)

    while q:
        loser = q.pop(0)
        visited[loser] = True
        for win in winners[loser]:
            if not visited[win]:
                if win not in winners[last]:
                    winners[last].append(win)
                    if last not in losers[win]:
                        losers[win].append(last)
                    last = loser
                    q.append(win)

    return answer


print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
