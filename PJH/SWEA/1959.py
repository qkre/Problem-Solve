import sys

sys.stdin = open("input/1959_input.txt", "r")

T = int(input())
result = []
for case in range(1, T + 1):
    N, M = map(int, input().split())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if N <= M:
        max_num = 0
        for i in range(M - N + 1):
            temp = 0
            C = B[i : i + N]
            for x, y in zip(A, B[i : i + N]):
                temp += x * y
            max_num = max(max_num, temp)

    else:
        max_num = 0
        for i in range(N - M + 1):
            temp = 0
            C = B[i : i + N]
            for x, y in zip(A[i : i + M], B):
                temp += x * y
            max_num = max(max_num, temp)

    result.append(f"#{case} {max_num}")

for _ in result:
    print(_)

output = open("output/1959_output.txt", "r").readlines()
output = [line.strip() for line in output]
print(result == output)
