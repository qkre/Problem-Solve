def solution(priorities, location):
    answer = 0

    from collections import deque

    processes = deque([chr(i) for i in range(65, 65+len(priorities))])
    priorities = deque(priorities)
    proceed = []

    target = processes[location]

    while priorities:
        priority = priorities.popleft()
        process = processes.popleft()
        if list(filter(lambda x: x > priority, priorities)):
            priorities.append(priority)
            processes.append(process)
        else:
            proceed.append((process, priority))
            if process == target:
                return len(proceed)

    return answer

solution([2, 1, 3, 2],	2)