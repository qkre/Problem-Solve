N = int(input())
result = []
for i in range(1, N//2 + 1):
    if N % i == 0 and i not in result:
        result.append(i)
        result.append(N // i)

result.sort()

print(*result)