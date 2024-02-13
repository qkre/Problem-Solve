answer = 0

def dfs(value, depth, numbers, target, length):
    global answer

    if depth == length:
        if target == value:
            answer += 1
        return

    dfs(value + numbers[depth], depth + 1, numbers, target, length)

    dfs(value - numbers[depth], depth + 1, numbers, target, length)

def solution(numbers, target):
    global answer


    dfs(0, 0, numbers, target, len(numbers))

    return answer


solution([1, 1, 1, 1, 1 ], 3)
