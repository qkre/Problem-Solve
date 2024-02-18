import sys

sys.stdin = open("input/2068_input.txt", "r")

T = int(input())
result = []
for case in range(1, T + 1):

    result.append(f"#{case} {max(list(map(int, input().split())))}")


for _ in result:
    print(_)

output = open("output/2068_output.txt", "r").readlines()
output = [line.strip() for line in output]
print(result == output)
