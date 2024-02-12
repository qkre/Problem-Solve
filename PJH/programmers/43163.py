def solution(begin, target, words):
    answer = float("inf")
    used = []

    from heapq import heappush, heappop

    q = [(begin, 0)]
    used.append(begin)
    while q:
        now, count = heappop(q)
        if now == target:
            answer = min(answer, count)

        for word in words:
            checked = False
            for i in range(len(word)):
                if list(now)[i] != list(word)[i]:
                    if checked:
                        checked = False
                        break
                    checked = True

            if checked and word not in used:
                used.append(word)
                heappush(q, (word, count+1))

    if answer == float("inf"):
        return 0

    return answer

solution("hit",	"cog",	["hot", "dot", "dog", "lot", "log", "cog"])