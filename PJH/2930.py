import os
import sys


current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"input/{current_file}_input.txt", "r", encoding="utf-8-sig")


result = []

T = int(input())

for case in range(1, T + 1):
    N = int(input())
    heap = [0]
    ans = []
    for _ in range(N):
        cmd = list(map(int, input().split()))
        if cmd[0] == 1:
            if len(heap) == 1:
                heap.append(cmd[1])
            else:
                heap.append(cmd[1])
                index = len(heap) - 1
                p = index // 2

                while heap[p] < cmd[1]:
                    tmp = heap[p]
                    heap[p] = cmd[1]
                    if index % 2 == 0:
                        heap[p * 2] = tmp
                    else:
                        heap[p * 2 + 1] = tmp

                    index = p
                    p = p // 2

                    if p < 1:
                        break
        else:
            if len(heap) >= 2:
                ans.append(heap[1])
                heap[1] = heap[-1]
                heap = heap[:-1]

                p = 1

                while p * 2 < len(heap):
                    checked = False
                    left = heap[p * 2]
                    right = heap[p * 2 + 1] if p * 2 + 1 < len(heap) else left

                    if left < right:
                        if right > heap[p]:
                            tmp = heap[p]
                            heap[p] = right
                            heap[p * 2 + 1] = tmp
                            checked = True
                            p = p * 2 + 1
                    else:
                        if left > heap[p]:
                            tmp = heap[p]
                            heap[p] = left
                            heap[p * 2] = tmp
                            checked = True
                            p = p * 2

                    if not checked:
                        break

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
