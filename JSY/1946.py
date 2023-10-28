import sys

sys.stdin = open("input/1946_input.txt")

t = int(input())

for c in range(t):
    n = int(input())
    ret = ""

    for i in range(n):
        char, cnt = input().split()
        ret += char * int(cnt)

    print(f"#{c+1}")
    for j in range(1, len(ret) + 1):
        print(ret[j - 1], end="")
        if j % 10 == 0:
            print("")
    print("")
