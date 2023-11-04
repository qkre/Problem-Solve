import os
import sys


current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"input/{current_file}_input.txt", "r", encoding="utf-8-sig")


result = []

T = int(input())

for case in range(1, T + 1):
    N = int(input())
    cards = list(input().split())

    shuffled = []

    if N % 2 == 0:
        head = cards[: N // 2]
        tail = cards[N // 2 :]
        for a, b in zip(head, tail):
            shuffled.append(a)
            shuffled.append(b)
    else:
        head = cards[: N // 2 + 1]
        tail = cards[N // 2 + 1 :]
        for i in range(N // 2):
            shuffled.append(head[i])
            shuffled.append(tail[i])
        shuffled.append(head[-1])

    result.append(f"#{case} {' '.join(shuffled)}")


for _ in result:
    print(_)


output = open(f"input/{current_file}_output.txt", "r").readlines()
output = [line.strip() for line in output]

print("------------------- 오답 ------------------ ( 이 아래로 출력이 없으면 정답)")

for r, o in zip(result, output):
    if r != o:
        print(f"정답 : {o},     오답 : {r}")
