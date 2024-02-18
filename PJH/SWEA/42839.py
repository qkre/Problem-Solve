def solution(numbers):
    answer = 0
    checked = []
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    numbers = list(numbers)

    import itertools

    for i in range(1, len(numbers)+1):
        perms = list(itertools.permutations(numbers, i))

        for perm in perms:
            perm = int(''.join(perm))
            if is_prime(perm) and perm not in checked:
                checked.append(perm)
                answer += 1


    return answer