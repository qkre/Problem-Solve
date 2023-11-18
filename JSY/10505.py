import sys

sys.stdin = open("C:/Users/jsio2/Computer/Algo/SWEA/input/10505_input.txt")
t = int(input())

for c in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    avg = int(sum(arr) // len(arr))
    cnt = 0

    for i in arr:
        if i <= avg:
            cnt +=1

    print(f"#{c+1} {cnt}")
