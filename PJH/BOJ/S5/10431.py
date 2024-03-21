from collections import deque


def solution():
    P = int(input())

    for _ in range(P):
        arr = deque(list(map(int, input().split())))
        case = arr.popleft()

        sorted_arr = []
        answer = 0
        while arr:
            std = arr.popleft()

            if not sorted_arr:
                sorted_arr.append(std)
            else:
                is_appended = False
                for i in range(len(sorted_arr)):
                    if std < sorted_arr[i]:
                        if i == 0:
                            sorted_arr = [std] + sorted_arr
                        else:
                            sorted_arr = sorted_arr[:i] + [std] + sorted_arr[i:]
                        answer += len(sorted_arr) - (i + 1)
                        is_appended = True
                        break
                if not is_appended:
                    sorted_arr.append(std)

        print(case, answer)

solution()