import sys

sys.stdin = open("input/1986_input.txt")

t = int(input())

for c in range(t):
    n = int(input())
    cnt = 0

    for i in range(1, n + 1):
        if i % 2 == 0:
            cnt -= i
        else:
            cnt += i

    print(f"#{c+1} {cnt}")
