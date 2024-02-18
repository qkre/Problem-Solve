import os
import sys


current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"input/{current_file}_input.txt", "r")





result = []

T = int(input())

for case in range(1, T+1):
    p, q = map(int, input().split())

    arr = list([1] * (max(p, q) + 3))

    
    for j in range(1, max(p, q) + 3):
        arr[j] = arr[j-1] + j
        if arr[j] > max(p, q):
            arr = arr[:j+1]
            break


    position_p = 0
    position_q = 0
    for i in range(max(p, q)):
        if p < arr[i+1]:
            position_p = [i+1, p - arr[i] + 1]
            break
    
    for i in range(max(p, q)):
        if q < arr[i+1]:
            position_q = [i+1, q-arr[i] + 1]
            break
    
    position_target = [position_p[0]+position_q[0], position_p[1]+position_q[1]]


    result.append(f"#{case} {arr[position_target[0]] + position_target[1]-1}")


for _ in result:
    print(_)

    






output = open(f"input/{current_file}_output.txt", "r").readlines()
output = [line.strip() for line in output]

print("------------------- 오답 ------------------ ( 이 아래로 출력이 없으면 정답)")

for r, o in zip(result, output):
    if r != o:
        print(f"정답 : {o},     오답 : {r}")



