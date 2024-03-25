from collections import defaultdict
def solution(id_list, report, k):
    answer = []

    reporter = defaultdict(set)
    reported = defaultdict(set)

    for i in range(len(report)):
        A, B = report[i].split()
        reporter[A].add(B)
        reported[B].add(A)

    for user_id in id_list:
        mail = 0
        for r in reporter[user_id]:
            if len(reported[r]) >= k:
                mail += 1

        answer.append(mail)

    print(answer)

    return answer


solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2)
