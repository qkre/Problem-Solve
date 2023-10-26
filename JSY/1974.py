import sys

sys.stdin = open("input/1974_input.txt")

t = int(input())

for cnt in range(1, t + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    state = 1
    # 가로 검사
    for i in range(1, 10, 1):
        for j in range(1, 10, 1):
            if arr[i - 1].count(j) >= 2:
                state = 0
                break
        if state == 0:
            break

    # 세로 검사
    for i in range(9):
        temp = []
        for j in range(9):
            temp.append(arr[j][i])

        for k in range(1, 10):
            if temp.count(k) >= 2:
                state = 0
                break

        if state == 0:
            break

    # 3*3 check
    for _ in range(0, 9, 3):
        temp = []
        for a in range(3):
            for b in range(3):
                temp.append(arr[a][b])

        for k in range(1, 10):
            if temp.count(k) >= 2:
                state = 0
                break

    if state == 0:
        print(f"#{cnt} 0")

    else:
        print(f"#{cnt} 1")
