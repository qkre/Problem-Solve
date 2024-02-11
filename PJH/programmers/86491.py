def solution(sizes):
    answer = 0

    w = [] # 가로, 세로 중 긴 부분
    h = [] # 가로, 세로 중 짧은 부분

    for s in sizes:
        w.append(max(s))
        h.append(min(s))

    return max(w) * max(h)


print(solution([[3, 4], [2, 1]]))
