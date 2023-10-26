from collections import deque
import sys

sys.stdin = open("input/1984_input.txt")

t = int(input())
for i in range(t):
    arr = deque(sorted(list(map(int, input().split()))))
    arr.popleft()
    arr.pop()
    print(f"#{i+1} {int(round(sum(arr)/len(arr),0))}")
