N = int(input())

is_sqrt = [False] * 50001
sqrt = []

for i in range(1, 50001):
    if i**2 > 50000:
        break
    is_sqrt[i**2] = True
    sqrt.append(i**2)

def lagrange(N, is_sqrt, sqrt):
    if is_sqrt[N]:
        return 1

    for i in sqrt:
        if i > N:
            break
        if is_sqrt[N - i]:
            return 2

    for i in range(len(sqrt)):
        if sqrt[i] > N:
            break
        for j in range(i, len(sqrt)):
            if sqrt[i] + sqrt[j] > N:
                break
            if is_sqrt[N - sqrt[i] - sqrt[j]]:
                return 3

    return 4

print(lagrange(N, is_sqrt, sqrt))