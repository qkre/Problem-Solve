from sys import stdin

input = stdin.readline

def early_start(A, B):
    if A[0] < B[0]:
        return True
    elif A[0] == B[0] and A[1] <= B[1]:
        return True

    return False

def early_end(A, B):
    if A[0] < B[0]:
        return True
    elif A[0] == B[0] and A[1] < B[1]:
        return True

    return False


def solution(N):
    answer = 0

    flowers = []

    for _ in range(N):
        sm, sd, em, ed = map(int, input().split())
        flowers.append([(sm, sd), (em, ed)])

    flowers.sort()

    for _ in flowers:
        print(_)

    start_arr = []
    end_arr = []

    possible = False

    for flower in flowers:
        S, E = flower
        if S == E:
            continue

        if not start_arr:
            if early_start(S, (3, 1)) and not early_end(E, (3, 1)):
                start_arr.append(S)
                end_arr.append(E)
                answer = 1
            continue

        if answer == 1:
            if early_start(S, (3, 1)) and not early_end(E, (3, 1)):
                if not early_end(E, end_arr[-1]):
                    start_arr[-1] = S
                    end_arr[-1] = E

            elif early_start(S, end_arr[-1]) and not early_end(E, end_arr[-1]):
                start_arr.append(S)
                end_arr.append(E)
                answer += 1
        else:
            if early_start(S, end_arr[-1]) and not early_end(E, end_arr[-1]):
                if early_start(S, end_arr[-2]):
                    start_arr[-1] = S
                    end_arr[-1] = E
                else:
                    start_arr.append(S)
                    end_arr.append(E)
                    answer += 1

        if not early_start(end_arr[-1], (11, 30)):
            possible = True
            break

    if not end_arr or not possible:
        answer = 0

    return answer


print(solution(int(input())))
