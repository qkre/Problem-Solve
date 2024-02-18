import sys

sys.stdin = open("SWEA/input/1859_input.txt", "r")


global prices

T = int(input())

for i in range(T):
    N = int(input())
    prices = list(map(int, input().split()))
    benefit = 0

    while len(prices) > 1:
        max_price_idx = prices.index(max(prices))

        head = prices[: max_price_idx + 1]
        prices = prices[max_price_idx + 1 :]

        for j in head:
            benefit += head[-1] - j

    print(f"#{i+1} {benefit}")
