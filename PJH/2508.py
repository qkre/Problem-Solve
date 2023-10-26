import sys

sys.stdin = open("input/2508_input.txt", "r")

N = list(map(int, list(input())))

print(sum(N))
