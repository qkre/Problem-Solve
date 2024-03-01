from sys import stdin
import itertools
input = stdin.readline


N, M = map(int, input().split())
arr = list(map(int, input().split()))
perms = list(set((itertools.permutations(arr, M))))
perms.sort()

for perm in perms:
    print(*perm)