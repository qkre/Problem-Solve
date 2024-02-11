def solution(answers):
    answer = []
    corrects = []
    supos = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]

    for supo in supos:
        idx = 0
        supo_idx = 0
        correct = 0
        while idx != len(answers):
            if supo[supo_idx] == answers[idx]:
                correct += 1

            idx += 1
            supo_idx += 1
            if supo_idx == len(supo):
                supo_idx = 0

        corrects.append(correct)

    max_correct = max(corrects)

    for i in range(3):
        if corrects[i] == max_correct:
            answer.append(i+1)

    return answer

solution([1, 2, 3, 4, 5])
