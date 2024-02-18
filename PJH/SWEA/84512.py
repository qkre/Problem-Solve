def solution(word):
    answer = 0

    alpha = list("AEIOU")
    dictionary = []

    def dfs(depth, length, alpha, value):
        if depth == length:
            dictionary.append(''.join(value))
            return

        for i in alpha:
            value.append(i)
            dfs(depth+1, length, alpha, value)
            value.pop()

    for length in range(1, 6):
        dfs(0, length, alpha, [])

    dictionary.sort()

    return dictionary.index(word) + 1

solution('')
