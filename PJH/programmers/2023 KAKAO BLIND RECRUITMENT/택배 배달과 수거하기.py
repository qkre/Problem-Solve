from collections import deque
def solution(cap, n, deliveries, pickups):
    answer = 0

    idps = [(i, d, p) for i, (d, p) in enumerate(zip(deliveries, pickups), 1) if d or p]


    delivery = 0
    pickup = 0
    while idps:
        i, d, p = idps.pop()
        delivery += d
        pickup += p
        while delivery > 0 or pickup > 0:
            delivery -= cap
            pickup -= cap
            answer += i*2
    print(answer)
    return answer


solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0])
solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0])
