from bisect import bisect_left, bisect_right

N, S, P = map(int, input().split())
try:
    ranks = list(map(int, input().split()))

    ranks.reverse()
    rank = -1
    if len(ranks) == P:
        if bisect_left(ranks, S) != 0:
            rank = P - bisect_right(ranks, S) + 1
    else:
        rank = len(ranks) - bisect_right(ranks, S) + 1

    print(rank)
except:
    print(1)