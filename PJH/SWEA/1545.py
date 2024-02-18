import sys

sys.stdin = open("input/1545_input.txt", "r")

T = int(input())
result = [i for i in range(T, -1, -1)]

print(*result)

