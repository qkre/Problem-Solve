import sys

sys.stdin = open("input/2063_input.txt")

n = int(input())
arr = sorted(list(map(int, input().split())))

print(arr[n // 2])
