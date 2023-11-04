import sys

sys.stdin = open("./input/1976_input.txt")
t = int(input())

for c in range(t):
    h1, m1, h2, m2 = map(int, input().split())

    hour = h1 + h2
    minute = m1 + m2

    if minute >= 60:
        hour += 1
        minute -= 60

    if hour == 24 or 12:
        hour = 12
    else:
        hour %= 12

    print(f"#{c+1} {hour} {minute}")
