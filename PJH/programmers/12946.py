def solution(n):
    answer = []

    def hanoi(N, FROM, TEMP, TO):
        if N == 1:
            answer.append([FROM, TO])
            return

        hanoi(N-1, FROM, TO, TEMP)
        answer.append([FROM, TO])
        hanoi(N-1, TEMP, FROM, TO)

    hanoi(n, 1, 2, 3)

    return answer

print(solution(3))