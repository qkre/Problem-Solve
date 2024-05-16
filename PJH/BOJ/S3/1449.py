N, L = map(int, input().split())
pos = list(map(lambda x: (x - 0.5, x + 0.5), map(int, input().split())))
pos.sort()

tapes = 0
coverage = 0
for min_x, max_x in pos:

    if coverage < max_x:
        coverage = min_x + L
        tapes += 1

print(tapes)