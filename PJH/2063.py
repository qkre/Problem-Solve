import sys

sys.stdin = open("input/2063_input.txt", "r")

T = int(input())

scores = list(map(int, input().split()))
scores.sort()

print(scores[T // 2])
