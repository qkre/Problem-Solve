def solution(num, total):
    for i in range(-1000, 1000):
        answer = []

        for j in range(num):
            answer.append(i + j)

        if sum(answer) == total: return answer



print(solution(3, 0))