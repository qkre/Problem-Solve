def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    index = -1
    while index + m < len(score):
        index += m
        answer += score[index] * m

    return answer

print(solution(4,	3,	[4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]))
