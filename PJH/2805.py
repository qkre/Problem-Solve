import sys

sys.stdin = open("input/2805_input.txt", "r")

T = int(input())
result = []
for case in range(1, T + 1):
    N = int(input())
    arr = list(list(map(int, input())) for _ in range(N))
    visited = list([0] * N for _ in range(N))
    ans = 0

    mid = N // 2
    for i in range(mid):
        harvest_start = mid - i
        harvest_end = mid + i + 1

        ans += sum(arr[i][harvest_start:harvest_end])

    ans += sum(arr[mid])

    for i in range(mid, 0, -1):
        harvest_start = mid - i + 1
        harvest_end = mid + i

        ans += sum(arr[N - i][harvest_start:harvest_end])

    result.append(f"#{case} {ans}")

    print(f"#{case} {ans}")


output = open("output/2805_output.txt", "r").readlines()
output = [line.strip() for line in output]
print(result == output)
