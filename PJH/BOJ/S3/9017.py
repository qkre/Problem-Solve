from collections import deque, defaultdict

T = int(input())


class Team:

    def __init__(self):
        self.number = None
        self.last_player = None
        self.total_score = 0
        self.count = 0


for case in range(T):
    N = int(input())
    ranks = deque(list(map(int, input().split())))
    team = defaultdict(Team)
    score = 1

    for i in ranks:
        if ranks.count(i) >= 6:
            if team[i].count < 4:
                team[i].number = i
                team[i].count += 1
                team[i].total_score += score
                score += 1
            elif team[i].count == 4:
                team[i].count += 1
                team[i].last_player = score
                score += 1
            else:
                score += 1

    team = list(team.items())
    team.sort(key=lambda x: (x[1].total_score, x[1].last_player))

    print(team[0][1].number)
