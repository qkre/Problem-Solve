answer = []
def dfs(used, tickets, ticket, path, length):
    global answer

    if False not in used:
        ans = path.copy()
        ans.append(ticket[1])
        answer.append(ans)
        return

    for i in range(length):
        if used[i]:
            continue

        if ticket[1] == tickets[i][0]:
            used[i] = True
            path.append(tickets[i][0])
            dfs(used, tickets, tickets[i], path, length)
            used[i] = False
            path.pop()

def solution(tickets):
    global answer

    length = len(tickets)

    for i in range(length):
        if tickets[i][0] == 'ICN':
            used = [False] * length
            used[i] = True
            dfs(used, tickets, tickets[i], [tickets[i][0]], length)


    answer.sort()

    return answer[0]

solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]])