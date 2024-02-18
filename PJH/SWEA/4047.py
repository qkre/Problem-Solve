import os
import sys


current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"input/{current_file}_input.txt", "r", encoding="utf-8-sig")


result = []

T = int(input())

for case in range(1, T + 1):
    cards = list(input())

    checked = list([False] * 13 for _ in range(4))
    err = False

    for i in range(0, len(cards), 3):
        card = cards[i : i + 3]

        if card[0] == "S":
            n = int("".join(card[1:])) - 1
            if not checked[0][n]:
                checked[0][n] = True
            else:
                err = True
                break

        elif card[0] == "D":
            n = int("".join(card[1:])) - 1
            if not checked[1][n]:
                checked[1][n] = True
            else:
                err = True
                break

        elif card[0] == "H":
            n = int("".join(card[1:])) - 1
            if not checked[2][n]:
                checked[2][n] = True
            else:
                err = True
                break

        elif card[0] == "C":
            n = int("".join(card[1:])) - 1
            if not checked[3][n]:
                checked[3][n] = True
            else:
                err = True
                break

    if not err:
        result.append(
            f"#{case} {checked[0].count(False)} {checked[1].count(False)} {checked[2].count(False)} {checked[3].count(False)}"
        )
    else:
        result.append(f"#{case} ERROR")


for _ in result:
    print(_)


output = open(f"input/{current_file}_output.txt", "r").readlines()
output = [line.strip() for line in output]

print("------------------- 오답 ------------------ ( 이 아래로 출력이 없으면 정답)")

for r, o in zip(result, output):
    if r != o:
        print(f"정답 : {o},     오답 : {r}")
