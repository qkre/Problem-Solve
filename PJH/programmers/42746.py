def solution(numbers):
    answer = ''

    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x + x * 3, reverse=True)

    return answer.join(numbers)


print(solution([3, 30, 34, 5, 9]))
