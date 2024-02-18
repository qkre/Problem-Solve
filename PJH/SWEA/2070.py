import sys

sys.stdin = open("input/2070_input.txt", "r")

T = int(input())
result = []
for case in range(1, T + 1):
    N, M = map(int, input().split())

    if N < M :
        print(f"#{case} <")
        result.append(f"#{case}<")
    elif N == M:
        print(f"#{case} =")
        result.append(f"#{case}=")
    else:
        print(f"#{case} >")
        result.append(f"#{case}>")


output = open("output/2070_output.txt", "r").readlines()
output = [line.strip() for line in output]
print(result == output)
