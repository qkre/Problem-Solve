def solution(n):
    answer = 0

    numbers = [i for i in range(1, 10001)]

    for i in range(0, n):
        for j in range(i+2, 10001):
            target = numbers[i:j]
            if n == sum(target):
                answer += 1
                break
            elif n < sum(target):
                break

    answer += 1

    return answer

print(solution(10))