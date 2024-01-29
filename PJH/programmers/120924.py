def solution(common):
    answer = 0

    l1 = common[-1] - common[-2]
    l2 = common[-2] - common[-3]

    if l1 == l2:
        answer = common[-1] + l1
    else:
        answer = common[-1] * (common[-1] // common[-2])

    return answer