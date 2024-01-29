def solution(quiz):
    answer = []

    for formular in quiz:
        formular = formular.split()

        X = int(formular[0])
        operator = formular[1]
        Y = int(formular[2])
        Z = int(formular[4])

        if operator == '+':
            if X + Y == Z:
                answer.append("O")
            else:
                answer.append("X")

        elif operator == "-":
            if X - Y == Z:
                answer.append("O")
            else:
                answer.append("X")



    return answer

print(solution(["3 - 4 = -3", "5 + 6 = 11"]))