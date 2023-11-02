result = []

N = 1000000


def prime_list(N):
    sieve = [True] * N

    m = int(N**0.5)

    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i + i, N, i):
                sieve[j] = False

    return [i for i in range(2, N) if sieve[i] == True]


print(*prime_list(N))
