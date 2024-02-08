def solution(n):
    # (a + b) % m = ((a % m) + (b % m)) % m
    # fib(n) = fib(n-1) + fib(n-2)
    # (fib(n-1) + fib(n-2)) % m = ((fib(n-1) % m) + (fib(n-2) % m)) % m


    fib = [0, 1]

    for i in range(2, n+1):
        fib.append(((fib[i-2] % 1234567) + (fib[i-1] % 1234567)) % 1234567)


    answer = fib[-1]

    return answer

