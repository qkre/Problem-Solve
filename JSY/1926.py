n = int(input())

arr = [str(i) for i in range(1, n + 1)]

for i in range(len(arr)):
    cnt = 0
    cnt = arr[i].count("3") + arr[i].count("6") + arr[i].count("9")

    if cnt >= 1:
        arr[i] = "-" * cnt

    print(arr[i], end=" ")
