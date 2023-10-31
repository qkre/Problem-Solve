import os
import sys


current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"input/{current_file}_input.txt", "r")


result = []

T = int(input())

for case in range(1, T + 1):
    N = int(input())

    arr = list(list(input()) for _ in range(N))
    ans = "NO"

    # row check
    for y in range(N):
        for x in range(0, N + 1, 5):
            if arr[y][x : x + 5].count("o") == 5:
                ans = "YES"
                break

    # col check
    for x in range(N):
        cnt = 0
        for y in range(0, N, 5):
            for k in range(5):
                if y + k >= N:
                    break
                if arr[y + k][x] == "o":
                    cnt += 1
            if cnt == 5:
                ans = "YES"
                break

    # diag check
    for y in range(N - 4):
        for x in range(N - 4):
            cnt = 0
            for i in range(5):
                if arr[y + i][x + i] == "o":
                    cnt += 1
            if cnt == 5:
                ans = "YES"
                break

        for x in range(N - 1, 3, -1):
            cnt = 0
            for i in range(5):
                if arr[y + i][x - i] == "o":
                    cnt += 1
            if cnt == 5:
                ans = "YES"
                break

    result.append(f"#{case} {ans}")


for _ in result:
    print(_)


output = open(f"input/{current_file}_output.txt", "r").readlines()
output = [line.strip() for line in output]

print("------------------- 오답 ------------------ ( 이 아래로 출력이 없으면 정답)")

for r, o in zip(result, output):
    if r != o:
        print(f"정답 : {o},     오답 : {r}")
