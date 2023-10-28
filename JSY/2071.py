import sys

sys.stdin = open("input/2071_input.txt")

t = int(input())

for c in range(t):
    arr = list(map(int, input().split()))

    print(f"#{c+1} {int(round(sum(arr)/len(arr),0))}")
