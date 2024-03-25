from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []

    def helper(course):
        counter = Counter()
        for order in orders:
            combs = list(map(lambda x: ''.join(sorted(x)),combinations(order, course)))
            counter.update(combs)

        max_frequency = 0
        for comb, freq in counter.most_common():
            if freq >= 2 and freq >= max_frequency:
                max_frequency = freq
                answer.append(comb)
            else:
                break
    for c in course:
        helper(c)

    print(answer)
    return answer


solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 5])
