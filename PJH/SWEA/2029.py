T = int(input())

for case in range(1, T+1):
    N, M = map(int, input().split())

    print(f"#{case} {N//M} {N%M}")