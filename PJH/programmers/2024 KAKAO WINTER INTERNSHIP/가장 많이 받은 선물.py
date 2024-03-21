from collections import defaultdict


def solution(friends, gifts):
    names = defaultdict(int)
    length = len(friends)

    for i in range(length):
        names[friends[i]] = i

    gift_info = [[0 for _ in range(length)] for _ in range(length)]
    totals = [0 for _ in range(length)]

    for info in gifts:
        giver, recipient = info.split()

        gift_info[names[giver]][names[recipient]] += 1
        totals[names[giver]] += 1
        totals[names[recipient]] -= 1

    next_month = [0 for _ in range(length)]

    for i in range(length):
        for j in range(i + 1, length):
            if gift_info[i][j] != 0:
                if gift_info[j][i] == 0:
                    next_month[i] += 1
                else:
                    if gift_info[i][j] < gift_info[j][i]:
                        next_month[j] += 1
                    elif gift_info[i][j] > gift_info[j][i]:
                        next_month[i] += 1
                    else:
                        if totals[i] < totals[j]:
                            next_month[j] += 1
                        elif totals[i] > totals[j]:
                            next_month[i] += 1
            elif gift_info[j][i] != 0:
                if gift_info[i][j] == 0:
                    next_month[j] += 1

            else:
                if totals[i] < totals[j]:
                    next_month[j] += 1
                elif totals[i] > totals[j]:
                    next_month[i] += 1

    print(next_month)


solution(["muzi", "ryan", "frodo", "neo"],
         ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"])
