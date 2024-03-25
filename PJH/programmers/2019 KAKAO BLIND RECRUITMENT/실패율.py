from collections import deque, defaultdict
def solution(N, stages):
    answer = []

    challenger = [0] * (N+1)

    for stage in stages:
        challenger[stage-1] += 1

    challenger = deque(challenger)
    peoples = len(stages)
    level = 1
    ratio = defaultdict(float)
    while challenger:
        n = challenger.popleft()

        if n == 0:
            ratio[level] = 0
        else:
            ratio[level] = n / peoples
        level += 1
        peoples -= n

    ratio = sorted(ratio.items(), key= lambda x: -x[1])
    print(ratio)
    for level, r in ratio:
        if level <= N:
            answer.append(level)
    print(answer)
    return answer

solution(5,	[2, 1, 2, 6, 2, 4, 3, 3])
solution(4,	[4,4,4,4,4])