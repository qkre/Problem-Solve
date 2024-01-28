def solution(lines):
    line = [0 for _ in range(-100, 101)]
    answer = 0

    for l in lines:
        for i in range(l[0]+1, l[1]+1):
            line[100 + i] += 1

    answer = len(line) - line.count(0) - line.count(1)

    return answer

print(solution([[0, 1], [2, 5], [3, 9]]))