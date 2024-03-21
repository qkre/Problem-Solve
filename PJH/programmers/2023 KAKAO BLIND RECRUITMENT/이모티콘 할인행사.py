from itertools import permutations

answer = []
def solution(users, emoticons):
    global answer

    n = len(emoticons)
    sales = [10, 20, 30, 40]
    comb = [0] * n

    def dfs(depth):
        global answer
        if depth == n:
            plus = 0
            sold = 0

            for i in range(len(users)):
                minimum, cost = users[i]
                paid = 0
                for j in range(n):
                    if minimum <= comb[j]:
                        paid += emoticons[j] * ((100 - comb[j]) / 100)

                if cost <= paid:
                    plus += 1
                else:
                    sold += paid

            answer = max(answer, [plus, sold])
            return

        for sale in sales:
            comb[depth] = sale
            dfs(depth + 1)


    dfs(0)

    print(answer)

    return answer

solution([[40, 10000], [25, 10000]],	[7000, 9000])