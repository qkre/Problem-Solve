t = int(input())

for c in range(t):
    n = int(input())
    arr = sorted(list(map(int, input().split())))

    print(f"#{c+1}", end=" ")
    for i in arr:
        print(i, end=" ")
    print()
