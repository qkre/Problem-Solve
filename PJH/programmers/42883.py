def solution(number, k):
    answer = ''

    number = list(number)

    count = 0
    answer_length = 0

    length = len(number) - k

    while answer_length < length:
        candidate = number[:-1 * length + 1]
        if candidate.count('9') > 0:
            answer += '9' * candidate.count('9')
            answer_length += candidate.count('9')
            for i in range(-1, -1 * len(candidate) - 1, -1):
                if candidate[i] == '9':
                    break
            number = number[len(candidate) + i + 1 : ]
            continue

        if not candidate:
            candidate = number

        answer += max(candidate)
        answer_length += 1
        number = number[candidate.index(max(candidate))+1:]


    return answer


print(solution("9898981234", 4))
