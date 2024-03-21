import itertools
from collections import defaultdict
from bisect import bisect_left, bisect_right


def get_sums(comb, dice, N):
    sums = []

    for i in range(6):
        d1 = dice[comb[0]]

        if N > 1:
            d2 = dice[comb[1]]
            for j in range(6):

                if N > 2:
                    d3 = dice[comb[2]]
                    for k in range(6):

                        if N > 3:
                            d4 = dice[comb[3]]
                            for l in range(6):

                                if N > 4:
                                    d5 = dice[comb[4]]
                                    for m in range(6):
                                        sums.append(d1[i] + d2[j] + d3[k] + d4[l] + d5[m])
                                else:
                                    sums.append(d1[i] + d2[j] + d3[k] + d4[l])
                        else:
                            sums.append(d1[i] + d2[j] + d3[k])
                else:
                    sums.append(d1[i] + d2[j])
        else:
            sums.append(d1[i])

    return sums


def solution(dice):
    answer = []

    N = len(dice)

    combs = list(itertools.combinations([i for i in range(N)], N // 2))
    results = defaultdict(list)

    A = combs
    B = combs

    max_wins = 0

    for a in A:
        if results[a]:
            continue
        for b in B:
            is_duplicate = False
            for _ in a:
                if _ in b:
                    is_duplicate = True
                    break
            if is_duplicate:
                continue
            a_sums = get_sums(a, dice, len(a))
            b_sums = get_sums(b, dice, len(b))

            a_sums.sort()
            b_sums.sort()

            a_keys = list(set(a_sums))
            a_keys.sort()

            wins = 0
            last_num = 0
            for num in a_keys:
                a_count = bisect_right(a_sums, num) - bisect_right(a_sums, last_num)
                b_count = bisect_left(b_sums, num)
                wins += a_count * b_count

                last_num = num
            if max_wins < wins:
                max_wins = wins
                answer = a

    print(max_wins)
    ans = []
    for i in answer:
        ans.append(i+1)

    print(ans)
    return ans

solution([[40, 41, 42, 43, 44, 45], [43, 43, 42, 42, 41, 41], [1, 1, 80, 80, 80, 80], [70, 70, 1, 1, 70, 70]])