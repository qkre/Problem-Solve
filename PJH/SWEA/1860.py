import os
import sys


current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"input/{current_file}_input.txt", "r")
result = []

T = int(input())


for case in range(1, T + 1):
    N, M, K = map(int, input().split())

    arr = list(map(int, input().split()))
    arr.sort()

    now = 0
    baking = 0
    time = 0
    while arr:

        if now >= len(arr):
            arr = []
            break

        if baking == M:
            baking = 0
            now += K
        
        if time == arr[0]:
            if now < arr.count(arr[0]):
                break
            else:
                now -= arr.count(arr[0])
                arr = arr[arr.count(arr[0]):]
        
        baking += 1
        time += 1
    
    if arr:
        result.append(f"#{case} Impossible")
    else:
        result.append(f"#{case} Possible")

for _ in result:
    print(_)

output = open(f"input/{current_file}_output.txt", "r").readlines()
output = [line.strip() for line in output]

print("------------------- 오답 ------------------ ( 이 아래로 출력이 없으면 정답)")

for r, o in zip(result, output):
    if r != o:
        print(f"정답 : {o},     오답 : {r}")

