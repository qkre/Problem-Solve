from sys import stdin

input = stdin.readline

def solution():
    T = int(input())

    for _ in range(T):
        N = int(input())
        arr = list(map(int, input().split()))
        max_cost = max(arr)
        max_day = N - 1 - list(reversed(arr)).index(max_cost)
        stocks = 0
        profit = 0
        for i in range(N):
            if i == N-1:
                profit += arr[i] * stocks

            elif i == max_day:
                profit += arr[i] * stocks
                stocks = 0

            else:
                if i < max_day:
                    stocks += 1
                    profit -= arr[i]
                else:
                    max_cost = max(arr[i:])
                    max_day = N - list(reversed(arr)).index(max_cost) - 1
                    if max_day != i:
                        stocks += 1
                        profit -= arr[i]
        print(profit)

solution()