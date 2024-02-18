import os
import sys

current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"input/{current_file}_input.txt", "r")

result = []


for case in range(1, 11):
    N = int(input())

    arr = list(list(map(int, input().split())) for _ in range(100))

    max_sum = 0

    for _ in arr:
        max_sum = max(max_sum, sum(_))

    for x in range(100):
        temp = 0
        for y in range(100):
            temp += arr[y][x]
        max_sum = max(max_sum, temp)

    temp = 0
    for i in range(100):
        temp += arr[i][i]

    max_sum = max(max_sum, temp)

    temp = 0
    for i in range(99, -1, -1):
        temp += arr[99 - i][i]

    max_sum = max(max_sum, temp)

    result.append(f"#{case} {max_sum}")

for i in result:
    print(i)

output = open(f"output/{current_file}_output.txt", "r").readlines()
output = [line.strip() for line in output]
print(result == output)
