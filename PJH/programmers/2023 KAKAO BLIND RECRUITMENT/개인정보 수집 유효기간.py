from collections import defaultdict


def solution(today, terms, privacies):
    answer = []
    types_to_month = defaultdict(int)
    for i in range(len(terms)):
        types, month = terms[i].split()
        types_to_month[types] = int(month)

    for i in range(len(privacies)):
        date, types = privacies[i].split()

        privacies[i] = (date, types)

    def date_distance(A, B):
        a_year, a_month, a_date = map(int, A.split('.'))
        b_year, b_month, b_date = map(int, B.split('.'))

        distance = (a_year * (28 * 12) + a_month * 28 + a_date) - (b_year * (28 * 12) + b_month * 28 + b_date)
        print(distance)
        return distance

    for i in range(len(privacies)):
        if types_to_month[privacies[i][1]] * 28 > date_distance(today, privacies[i][0]):
            continue
        else:
            answer.append(i + 1)

    print(answer)

    return answer


solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"])
solution("2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"])
