import sys
from collections import defaultdict
sys.setrecursionlimit(10**5)
def find(rooms, want):
    room = want
    if rooms[room]:
        room = find(rooms, rooms[room])
    rooms[want] = room + 1
    return room


def solution(k, room_number):
    answer = []

    rooms = defaultdict(int)

    for want in room_number:
        answer.append(find(rooms, want))

    print(answer)

    return answer


solution(10, [1, 3, 4, 1, 3, 1, 1, 1, 1])
