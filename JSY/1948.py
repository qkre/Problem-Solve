import sys

sys.stdin = open("./input/1948_input.txt")
t = int(input())
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for c in range(t):
    ret = 0
    m1, d1, m2, d2 = map(int, input().split())
    if m1 == m2:
        ret = d2 - d1 + 1
    else:
        ret = month[m1 - 1] - d1 + 1
        for i in range(m1 + 1, m2):
            ret += month[i - 1]

        ret += d2
    print(f"#{c+1} {ret}")
