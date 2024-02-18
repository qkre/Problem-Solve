import os
import sys


current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"input/{current_file}_input.txt", "r")


result = []

T = int(input())

decode_list = [
    "0001101",
    "0011001",
    "0010011",
    "0111101",
    "0100011",
    "0110001",
    "0101111",
    "0111011",
    "0110111",
    "0001011",
]

for case in range(1, T + 1):
    N, M = map(int, input().split())

    arr = list(list(input()) for _ in range(N))

    for row in arr:
        if "1" in row:
            code = row
            break

    first_index = code.index("1")
    temp = "".join(code[first_index : first_index + 7])

    while not temp in decode_list:
        first_index -= 1
        temp = "".join(code[first_index : first_index + 7])

    decode = 0
    odd = 0

    for i in range(1, 9):
        start = first_index + 7 * (i - 1)
        end = first_index + 7 * i

        s = "".join(code[start:end])

        if i % 2 == 1:
            odd += decode_list.index(s)
        else:
            decode += decode_list.index(s)

    decode += odd * 3
    if decode % 10 == 0:
        result.append(f"#{case} {decode - (odd*2)}")
    else:
        result.append(f"#{case} 0")


for _ in result:
    print(_)


output = open(f"input/{current_file}_output.txt", "r").readlines()
output = [line.strip() for line in output]

print("------------------- 오답 ------------------ ( 이 아래로 출력이 없으면 정답)")

for r, o in zip(result, output):
    if r != o:
        print(f"정답 : {o},     오답 : {r}")
