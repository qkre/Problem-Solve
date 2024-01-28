def solution(a, b, c, d):
    answer = 0

    numbers = {a : 0, b : 0, c : 0, d : 0};


    numbers[a] += 1
    numbers[b] += 1
    numbers[c] += 1
    numbers[d] += 1

    numbers = sorted(numbers.items(), key=lambda item: item[1])

    if len(numbers) == 1:
        return 1111 * numbers[0][0]

    elif len(numbers) == 2 and numbers[0][1] != numbers[1][1]:
        return (10 * numbers[1][0] + numbers[0][0])**2
    elif len(numbers) == 2 and numbers[0][1] == 2:
        return (numbers[0][0] + numbers[1][0]) * abs(numbers[0][0] - numbers[1][0])
    elif len(numbers) == 3:
        return numbers[0][0] * numbers[1][0]
    else:
        return min(a, b, c, d)


    return answer

print(solution(2, 2, 2, ))