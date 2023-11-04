t = int(input())

for c in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    for i in range(len(arr)):
        arr[i] = abs(arr[i])
    ret = min(arr)
    cnt = arr.count(ret)

    print(f"#{c+1} {ret} {cnt}")
