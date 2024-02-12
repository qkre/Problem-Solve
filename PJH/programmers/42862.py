def solution(n, lost, reserve):
    answer = n

    lost.sort()
    reserve.sort()

    for l in lost.copy():
        if l in reserve.copy():
            lost.remove(l)
            reserve.remove(l)

    borrow = []
    used = []

    for l in lost:
        for r in reserve:
            if l - 1 <= r <= l + 1 and r not in used:
                borrow.append(l)
                used.append(r)
                break

    answer -= (len(lost) - len(borrow))

    return answer


print(solution(5, [4, 3], [3, 4]))
