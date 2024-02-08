def solution(citations):
    n = len(citations)
    answer = 0
    for i in range(0, n+1):
        over = len(list(filter(lambda x : x >= i, citations)))

        if over >= i:
            answer = i

    return answer

print(solution([3, 5, 6, 1, 5]))
