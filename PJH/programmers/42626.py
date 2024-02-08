def solution(scoville, K):
    answer = 0

    scoville.sort()

    import heapq

    heapq.heapify(scoville)

    while scoville[0] < K and len(scoville) > 1:
        A = heapq.heappop(scoville)
        B = heapq.heappop(scoville)

        heapq.heappush(scoville, A + B*2)
        answer += 1

    if scoville[0] < K:
        return -1

    return answer


print(solution([1, 1, 2, 10], 24))