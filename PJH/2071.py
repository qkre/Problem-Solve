T = int(input())

for case in range(1, T + 1):
    N = int(input())
    scores = list(map(int, input().split()))

    average = 0

    for i in scores:
        average += i

    average /= N

    print(f"#{case} {average}")
