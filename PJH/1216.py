import os
import sys

current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"input/{current_file}_input.txt", "r")


result = []



for case in range(1, 11):
    N = int(input())
    arr = list(list(input()) for _ in range(100))

    max_len = 0

    # col check
    for y in range(100):
        for i in range(100):
            for j in range(1, 102):
                if i+j > 100:
                    break
                a = arr[y][i : i+j]
                if arr[y][i : i+j] == list(reversed(arr[y][i : i+j])):
                    max_len = max(max_len, len(a))

    for x in range(100):
        for i in range(100):
            temp = []
            for j in range(100):
                if i+j >= 100:
                    break
                temp.append(arr[i+j][x])
                if temp == list(reversed(temp)):
                    max_len = max(max_len, len(temp))


    result.append(f"#{case} {max_len}")

for _ in result:
    print(_)

output = open(f"output/{current_file}_output.txt", "r").readlines()
output = [line.strip() for line in output]
print(result == output)
