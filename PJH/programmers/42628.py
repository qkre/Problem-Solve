def solution(operations):

    import heapq

    max_heap = []
    min_heap = []

    while operations:
        operation = operations[0]

        cmd, num = operation.split()[0], int(operation.split()[1])

        if cmd == 'I':
            heapq.heappush(max_heap, -1 * num)
            heapq.heappush(min_heap, num)

        if cmd == 'D':
            if len(max_heap) == 0:
                operations = operations[1:]
                continue

            if num == -1:
                target = heapq.heappop(min_heap)
                temp = []
                while True:
                    t = heapq.heappop(max_heap)
                    if target != t*-1:
                        temp.append(t)
                    else:
                        break
                while temp:
                    heapq.heappush(max_heap, temp.pop())
            else:
                target = heapq.heappop(max_heap)
                temp = []
                while True:
                    t = heapq.heappop(min_heap)
                    if target != t*-1:
                        temp.append(t)
                    else:
                        break
                while temp:
                    heapq.heappush(min_heap, temp.pop())


        operations = operations[1:]

    if len(max_heap) == 0:
        return [0, 0]

    return [heapq.heappop(max_heap) * -1 , heapq.heappop(min_heap)]

solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"])