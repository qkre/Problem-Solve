import sys

sys.stdin = open("input/2071_input.txt", "r")

T = int(input())

for case in range(1, T + 1):
    scores = list(map(int, input().split()))

    average = 0

    for i in scores:
        average += i

    average /= len(scores)

    print(f"#{case} {round(average)}")
