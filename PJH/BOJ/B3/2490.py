
for _ in range(3):
    arr = list(map(int, input().split()))
    count = arr.count(0)
    if count == 0:
        print("E")
    elif count == 1:
        print("A")
    elif count == 2:
        print("B")
    elif count == 3:
        print("C")
    else:
        print("D")