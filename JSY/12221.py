t = int(input())

for c in range(t):
    n, m = map(int, input().split())

    if n >= 10 or m >= 10:
        print(f"#{c+1} -1")

    else:
        print(f"#{c+1} {n*m}")