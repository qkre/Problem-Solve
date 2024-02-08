def solution(n):
    f = [1, 2]

    if n == 1:
        return 1

    # (a+b) % m = ((a % m) + (b % m)) % m
    # f(n) % m = (f(n-1) + f(n-2)) % m = ((f(n-1) % m) + (f(n-2) % m)) % m

    for i in range(2, n):
        f.append(((f[i - 1] % 1234567) + (f[i - 2] % 1234567)) % 1234567)



    return f[-1]

print(solution(2000))