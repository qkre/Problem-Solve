import sys

sys.stdin = open("input/1859_input.txt")

t = int(input())

for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    maxprice = 0
    ret = 0
    
    for j in arr[::-1]:
        if j >= maxprice:
            maxprice = j
            
        else:
            ret += (maxprice - j)
    print(f"#{i+1} {ret}")