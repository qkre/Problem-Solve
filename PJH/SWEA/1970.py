import os
import sys


current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"input/{current_file}_input.txt", "r")




result = []

T = int(input())

for case in range(1, T+1):
    N = int(input())
    arr = [0] * 8
    while N >= 10 :

        arr[0] = N // 50000
        N -= 50000 * arr[0]

        arr[1] = N // 10000
        N -= 10000 * arr[1]

        arr[2] = N // 5000
        N -= 5000 * arr[2]

        arr[3] = N // 1000
        N -= 1000 * arr[3]

        arr[4] = N // 500
        N -= 500 * arr[4]

        arr[5] = N // 100
        N -= 100 * arr[5]
        
        arr[6] = N // 50
        N -= 50 * arr[6]

        arr[7] = N // 10
        N -= 10 * arr[7]
    
    result.append(f"#{case}")
    result.append(' '.join(map(str,arr)))
        


for _ in result:
    print(_)

output = open(f"input/{current_file}_output.txt", "r").readlines()
output = [line.strip() for line in output]

print("------------------- 오답 ------------------ ( 이 아래로 출력이 없으면 정답)")

for r, o in zip(result, output):
    if r != o:
        print(f"정답 : {o},     오답 : {r}")



