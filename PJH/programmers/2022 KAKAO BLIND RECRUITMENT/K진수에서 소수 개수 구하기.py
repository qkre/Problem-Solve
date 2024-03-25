
def is_prime(n):
    if n <= 1:
        return False
    i = 2

    while i**2 <= n:
        if n % i == 0:
            return False
        i += 1

    return True

def solution(n, k):
    answer = 0

    rev_base = ''

    while n > 0:
        n, mod = divmod(n, k)
        rev_base += str(mod)
    rev_base = ''.join(reversed(rev_base))
    stack = list(rev_base.split('0'))


    for i in stack:
        if not i:
            continue
        if is_prime(int(i)):
            answer += 1

    return answer


solution(110011, 10)