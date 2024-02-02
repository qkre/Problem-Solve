def solution(progresses, speeds):
    answer = []

    from collections import deque
    progresses = deque(progresses)
    speeds = deque(speeds)
    day = 0

    while progresses:
        day += 1
        release = 0

        while progresses:
            if progresses[0] >= 100:
                progresses.popleft()
                speeds.popleft()
                release += 1
            else:
                break

        if release > 0:
            answer.append(release)

        for i in range(len(progresses)):
            progresses[i] += speeds[i]

    return answer


solution([93, 30, 55], [1, 30, 5])
