import sys

sys.stdin = open("./input/1970_input.txt")
t = int(input())

for c in range(t):
    money = int(input())
    arr = [0 for _ in range(8)]

    arr[0] = money // 50000
    money %= 50000

    arr[1] = money // 10000
    money %= 10000

    arr[2] = money // 5000
    money %= 5000

    arr[3] = money // 1000
    money %= 1000

    arr[4] = money // 500
    money %= 500

    arr[5] = money // 100
    money %= 100

    arr[6] = money // 50
    money %= 50

    arr[7] = money // 10

    print(f"#{c+1}")
    for i in arr:
        print(f"{i}", end=" ")
    print()
