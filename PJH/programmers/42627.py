def solution(jobs):
    import heapq

    jobs.sort()
    count, last = 0, -1
    wait = []
    time = jobs[0][0]
    length = len(jobs)
    answer = 0

    while count < length:
        for s, t in jobs:
            if last < s <= time:
                heapq.heappush(wait, (t, s))
        if len(wait) > 0:
            last = time
            term, start = heapq.heappop(wait)
            count += 1
            time += term
            answer += (time - start)
        else:
            time += 1

    return answer // count

print(solution([[0, 3], [1, 9], [4, 2], [2, 6]]))
