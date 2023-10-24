n, k = map(int, input().split())

arr = [1, 2]
for _ in range(n - 2):
    arr.append(0)

i = 0

for a in range(k - 1):
    if arr[i] == 1 and arr[i + 1] == 2:
        temp = arr[i + 1]
        arr[i + 1] = arr[i + 2]
        arr[i + 2] = temp

        for j in range(i, 0, -1):
            arr[j] = 0
            arr[0] = 1
        i = 0

    elif arr[i] == 1 and arr[i + 1] == 0:
        temp = arr[i]
        arr[i] = arr[i + 1]
        arr[i + 1] = temp

        i += 1

    else:
        i += 1
        for j in range(i, 1, -1):
            arr[j] = 0
    print(a, arr)


print(arr)
cnt = 1
for i in range(len(arr) - 1, 0, -1):
    if arr[i] == 1:
        print(cnt)
        break
    else:
        cnt += 1
