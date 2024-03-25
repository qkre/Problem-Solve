answer = 0
ban = []
def dfs(depth, user_list, banned_list):
    global answer, ban
    if depth == len(banned_list):
        if set(user_list) in ban:
            return
        ban.append(set(user_list))
        print(ban)
        answer += 1
        return

    for name in banned_list[depth]:
        if name not in user_list:
            user_list.append(name)
            dfs(depth + 1, user_list, banned_list)
            user_list.pop()

def solution(user_id, banned_id):
    global answer, ban
    answer = 0
    ban = []

    banned_list = [[] for _ in range(len(banned_id))]


    for i in range(len(user_id)):
        uid = user_id[i]

        for j in range(len(banned_id)):
            bid = banned_id[j]

            if len(uid) == len(bid):
                uid_lst = list(uid)
                bid_lst = list(bid)

                is_banned = True

                while uid_lst:
                    u, b = uid_lst.pop(), bid_lst.pop()

                    if b == '*' or u == b:
                        continue
                    else:
                        is_banned = False
                        break

                if is_banned:
                    banned_list[j].append(user_id[i])


    dfs(0, [], banned_list)

    print(answer)


    return answer

solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],	["fr*d*", "abc1**"])
solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],	["*rodo", "*rodo", "******"])
solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],	["fr*d*", "*rodo", "******", "******"])