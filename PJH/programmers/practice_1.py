def solution(X, Y):
    answer = ""

    count_X = []
    count_Y = []
    candidate = []
    for i in range(10):
        count_X.append(list(X).count(f"{i}"))
        count_Y.append(list(Y).count(f"{i}"))

    for i in range(10):
        if count_X[i] == 0 or count_Y[i] == 0:
            candidate.append(0)
            continue

        candidate.append(min(count_X[i], count_Y[i]))

    for i in range(9, -1, -1):
        answer += candidate[i] * f"{i}"

    if answer == "":
        answer = "-1"

    if answer.startswith("0"):
        answer = "0"

    return answer

X, Y = input().split()

print(solution(X, Y))