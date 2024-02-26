from sys import stdin
input = stdin.readline

def solution():
    N, S, R = map(int, input().split())
    broken = list(map(int, input().split()))
    pair = list(map(int, input().split()))
    answer = 0

    while True:
        cheked = False
        for i in broken:
            if i in pair:
                cheked = True
                pair.remove(i)
                broken.remove(i)
                break
        if not cheked:
            break

    for b in broken:
        if b-1 in pair:
            pair.remove(b-1)
        elif b+1 in pair:
            pair.remove(b+1)
        else:
            answer += 1

    return answer

print(solution())