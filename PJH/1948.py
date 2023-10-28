import os
import sys


current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"input/{current_file}_input.txt", "r")
result = []

T = int(input())

dates = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for case in range(1, T+1):
    arr = list(map(int, input().split()))

    date = 0
    if arr[0] == arr[2]:
        date += arr[3]
    else:
        date += dates[arr[0] - 1] - arr[1]
        for i in range(1, arr[2] - arr[0]):
            date += dates[arr[0] + i -1]
        date += arr[3] + 1
    
    result.append(f"#{case} {date}")


for _ in result:
    print(_)

output = open(f"input/{current_file}_output.txt", "r").readlines()
output = [line.strip() for line in output]

print("------------------- 오답 ------------------ ( 이 아래로 출력이 없으면 정답)")

for r, o in zip(result, output):
    if r != o:
        print(f"정답 : {o},     오답 : {r}")


