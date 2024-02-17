def solution(k, tangerine):
    answer = 0
    count = {}

    for t in tangerine:
        if t not in count:
            count[t] = 1
        else:
            count[t] += 1

    tangerine = sorted(list(count.items()), key= lambda x:x[1], reverse=True)

    for n, c in tangerine:
        k -= c
        answer += 1
        if k <= 0:
            break

    return answer

solution(1,	[1,1])