answer = 0


def solution(numbers, target):
    global answer
    def dfs(value, depth):
        global answer
        if depth == len(numbers):
            if target == value:
                answer += 1
            return

        dfs(value + numbers[depth], depth+1)
        dfs(value - numbers[depth], depth+1)


    dfs(0, 0)

    return answer


solution([1, 1, 1, 1, 1 ], 3)
