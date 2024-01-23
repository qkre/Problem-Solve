import math


def solution(n):
    answer = 0
    if n == 1:
        return 1

    for i in range(1, math.ceil(n**0.5)):
        if n % i == 0:
            answer += i
            answer += n // i

    return answer

print(solution(1))