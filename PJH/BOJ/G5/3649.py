from bisect import bisect_left, bisect_right

while True:
    try:
        X = int(input())
        N = int(input())

        X *= 1e7

        bricks = list(int(input()) for _ in range(N))
        bricks.sort()
        ans = False

        while bricks:
            brick = bricks.pop()

            if bisect_left(bricks, X-brick) != bisect_right(bricks, X - brick):
                print(f"yes {int(X - brick)} {brick}")
                ans = True
                break
        if not ans:
            print("danger")
    except:
        break