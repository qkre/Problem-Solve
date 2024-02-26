from sys import stdin
from heapq import heappop, heappush, heapify

input = stdin.readline


def solution():
    N, M = map(int, input().split())
    cards = list(map(int, input().split()))
    heapify(cards)

    for _ in range(M):
        A, B = heappop(cards), heappop(cards)
        heappush(cards, A + B)
        heappush(cards, A + B)

    print(sum(cards))


solution()
