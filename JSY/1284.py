t = int(input())

for c in range(t):
    p, q, r, s, w = map(int, input().split())

    A = p * w

    if r < w:
        B = q + ((w - r) * s)

    else:
        B = q

    if A > B:
        print(f"#{c+1} {B}")

    else:
        print(f"#{c+1} {A}")
