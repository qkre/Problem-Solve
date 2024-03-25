def solution(places):
    answer = []

    for place in places:

        peoples = []

        for r in range(5):
            for c in range(5):
                if place[r][c] == 'P':
                    peoples.append((r, c))

        protected = True

        for i in range(len(peoples)):
            p1 = peoples[i]
            for j in range(i+1, len(peoples)):
                if i == j:
                    continue

                p2 = peoples[j]
                distance = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

                if distance == 1:
                    protected = False
                    break

                if distance == 2:

                    if p1[0] == p2[0]:
                        if place[p1[0]][p1[1] + 1] == 'O':
                            protected = False
                            break
                    elif p1[1] == p2[1]:
                        if place[p1[0] + 1][p1[1]] == 'O':
                            protected = False
                            break
                    else:
                        if p1[0] < 4:
                            if place[p1[0] + 1][p1[1]] == 'O':
                                protected = False
                                break

                        if p1[1] < p2[1]:
                            if p1[1] < 4:
                                if place[p1[0]][p1[1] + 1] == 'O':
                                    protected = False
                                    break
                        else:
                            if p1[1] > 0:
                                if place[p1[0]][p1[1] - 1] == 'O':
                                    protected = False
                                    break

                if not protected:
                    break
            if not protected:
                break

        if protected:
            answer.append(1)
        else:
            answer.append(0)

    print(answer)

    return answer

solution( [["POOOP", "OXXOX", "OXXPX", "OPXOX", "PXXXP"]])