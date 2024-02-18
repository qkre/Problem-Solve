T = int(input())

for case in range(1, T+1):
    N = int(input())

    arr = list(map(int, input().split()))
    arr.sort()
    a = ' '.join(map(str, arr))
    print(f"#{case} {a}")