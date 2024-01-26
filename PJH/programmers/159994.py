def solution(cards1, cards2, goal):
    answer = 'Yes'

    last_index = -1
    for word in cards1.copy():
        if goal.count(word) > 0:
            if cards1.index(word) != 0 or last_index > goal.index(word):
                answer ="No"
                break
            last_index = goal.index(word)
            cards1.remove(word)
            goal[last_index] = True

    last_index = -1
    for word in cards2.copy():
        if goal.count(word) > 0:
            if cards2.index(word) != 0 or last_index > goal.index(word):
                answer ="No"
                break
            last_index = goal.index(word)
            cards2.remove(word)
            goal[last_index] = True


    return answer

print(solution( ["i", "water", "drink"]	,["want", "to"]	,["i", "want", "to", "drink", "water"]))