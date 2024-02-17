def solution(n):
    answer = n
    n = format(n, 'b')
    cnt = n.count('1')

    while True:
        answer += 1
        temp = format(answer, 'b')
        if temp.count('1') == cnt:
            break

    return answer



solution(78)