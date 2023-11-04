import sys

sys.stdin = open("./input/1288_input.txt")

t = int(input())

for c in range(t):
    n = int(input())
    i = 1
    ret = set()
    while True:
        for j in list(str(n)):
            ret.add(j)

        if len(ret) == 10:
            break
        n //= i
        i += 1
        n *= i

    print(f"#{c+1} {n}")
