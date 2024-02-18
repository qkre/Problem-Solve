import os
import sys


current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"input/{current_file}_input.txt", "r")





result = []

T = int(input())

for case in range(1, T+1):
    N = int(input())
    
    s = ''
    result.append(f"#{case}")
    for _ in range(N):
        c, k = input().split()
        s += c * int(k)
    
    for i in range(0, len(s)+1, 10):
        result.append(s[i : i+10])
    
    

for _ in result:
    print(_)






output = open(f"input/{current_file}_output.txt", "r").readlines()
output = [line.strip() for line in output]

print("------------------- 오답 ------------------ ( 이 아래로 출력이 없으면 정답)")

for r, o in zip(result, output):
    if r != o:
        print(f"정답 : {o},     오답 : {r}")



