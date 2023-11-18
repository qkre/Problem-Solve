t = int(input())

for c in range(t):
    n , m = map(int, input().split())
    print(f"#{c+1} {(n+m) % 24}")