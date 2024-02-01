def solution(genres, plays):
    answer = []

    ranks = {}

    index = 0

    for (genre, play) in zip(genres, plays):

        if ranks.get(genre):
            ranks[genre].append((index, play))
        else:
            ranks[genre] = [(index, play)]

        index += 1

    for genre in set(genres):
        ranks[genre].sort(key=lambda x:x[1], reverse=True)



    sorted_ranks = dict(sorted(ranks.items(), key=lambda x: sum(y[1] for y in x[1]), reverse= True))

    for genre in list(sorted_ranks.keys()):
        count = 0
        while count < 2 and count < len(ranks[genre]):
            answer.append(ranks[genre][count][0])
            count += 1


    return answer

print(solution(["classic", "classic", "classic", "pop"],	[ 600, 150, 800, 2500]))