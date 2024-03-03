from sys import stdin
import itertools

input = stdin.readline

def solution():
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    arr = list(set(arr))
    arr.sort()


    perms = list(itertools.combinations_with_replacement(arr, M))

    for _ in perms:
        print(*_)

solution()