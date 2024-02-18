import sys

sys.stdin = open("input/1204_input.txt", "r")

T = int(input())

for case in range(1, T + 1):
    N = int(input())
    scores = list(map(int, input().split()))

    max_score = 0

    for i in range(101):
        if scores.count(max_score) <= scores.count(i):
            max_score = i

    print(f"#{case} {max_score}")
