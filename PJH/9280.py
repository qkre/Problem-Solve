import os
import sys


current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"input/{current_file}_input.txt", "r")


result = []

T = int(input())

for case in range(1, T + 1):
    N, M = map(int, input().split())
    R = list(int(input()) for _ in range(N))
    W = list(int(input()) for _ in range(M))

    parking = {}
    parked = [False] * N
    waiting = []
    cost = 0
    for _ in range(2 * M):
        x = int(input())

        if x >= 0:
            checked = False
            for i in range(N):
                if not parked[i]:
                    parked[i] = True
                    parking[W[x - 1]] = i
                    checked = True
                    break
            if not checked:
                waiting.append(W[x - 1])
        else:
            x *= -1
            cost += R[parking[W[x - 1]]] * W[x - 1]
            parked[parking[W[x - 1]]] = False

            if waiting:
                parked[parking[W[x - 1]]] = True
                parking[waiting[0]] = parking[W[x - 1]]
                waiting = waiting[1:]

            del parking[W[x - 1]]

    result.append(f"#{case} {cost}")


for _ in result:
    print(_)


output = open(f"input/{current_file}_output.txt", "r").readlines()
output = [line.strip() for line in output]

print("------------------- 오답 ------------------ ( 이 아래로 출력이 없으면 정답)")

for r, o in zip(result, output):
    if r != o:
        print(f"정답 : {o},     오답 : {r}")
