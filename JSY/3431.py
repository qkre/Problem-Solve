t = int(input())

for c in range(t):
    l, u, x = map(int, input().split())

    if x < l:
        print(f"#{c+1} {l-x}")

    elif x > u:
        print(f"#{c+1} -1")

    else:
        print(f"#{c+1} 0")