answer = [-1]
max_distance = 0
def dfs(score, now, state, info, n):
    global  answer, max_distance
    if now == 0:
        apeach_score = 0
        lion_score = 0
        for i in range(11):
            if info[i] < state[i]:
                lion_score += 10 - i
            elif state[i] < info[i] and 0 < info[i]:
                apeach_score += 10 - i

        if apeach_score < lion_score:
            if max_distance < lion_score - apeach_score:
                max_distance = lion_score - apeach_score
                answer = state.copy()
            elif max_distance == lion_score - apeach_score:
                temp_answer = answer.copy()
                temp_state = state.copy()

                while temp_answer:
                    a = temp_answer.pop()
                    b = temp_state.pop()

                    if a and not b:
                        break
                    if b and not a:
                        answer = state.copy()
                        break



        return

    for i in range(score, 11):
        if info[i] < now:
            state[i] = info[i] + 1
            dfs(i+1, now - state[i], state.copy(), info, n)
            state[i] = 0
    if now:
        state[-1] = now
        dfs(11, 0, state.copy(), info, n)

def solution(n, info):
    global answer, max_distance
    answer = [-1]
    max_distance = 0

    dfs(0, n, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], info, n)

    print(answer)
    return answer
# answer : [1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0]
solution(3, [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1])