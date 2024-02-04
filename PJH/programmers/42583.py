def solution(bridge_length, weight, truck_weights):
    answer = 0

    from collections import deque

    trucks = deque([chr(65 + i) for i in range(len(truck_weights))])
    truck_weights = deque(truck_weights)
    bridge_status = {}

    time = 0

    while truck_weights:

        time += 1

        items = list(bridge_status.items())

        weight_sum = 0

        for truck, data in items:
            weight_sum += data[0]

        if weight_sum + truck_weights[0] <= weight:
            bridge_status[trucks.popleft()] = (truck_weights.popleft(), 1)


        for truck in list(bridge_status.keys()):
            w, t = bridge_status[truck][0], bridge_status[truck][1]
            if t + 1 > bridge_length:
                del bridge_status[truck]
                continue

            bridge_status[truck] = (w, t + 1)


    while bridge_status:
        time += 1

        for truck in list(bridge_status.keys()):
            w, t = bridge_status[truck][0], bridge_status[truck][1]
            if t + 1 > bridge_length:
                del bridge_status[truck]
                continue

            bridge_status[truck] = (w, t + 1)



    return time+1

print(solution(100,	100,	[10,10,10,10,10,10,10,10,10,10]))