import os
import sys


current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"input/{current_file}_input.txt", "r", encoding="utf-8-sig")


import heapq

result = []

T = int(input())

for case in range(1, T + 1):
    N = int(input())
    heap = []
    ans = []
    for _ in range(N):
        cmd = list(map(int, input().split()))

        if cmd[0] == 1:
            heapq.heappush(heap, -cmd[1])
        else:
            if len(heap) > 0:
                ans.append(-heapq.heappop(heap))
            else:
                ans.append(-1)
    
    result.append(f"#{case} {' '.join(list(map(str, ans)))}")


for _ in result:
    print(_)


output = open(f"input/{current_file}_output.txt", "r").readlines()
output = [line.strip() for line in output]

print("------------------- 오답 ------------------ ( 이 아래로 출력이 없으면 정답)")

for r, o in zip(result, output):
    if r != o:
        print(f"정답 : {o},     오답 : {r}")
