def solution(s):
    answer = 1
    if len(s) % 2 != 0:
        return 0
    stack = []
    for i in s:
        if not stack:
            stack.append(i)
        else:
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)

    if len(stack) != 0:
        answer = 0
    return answer


print(solution("b" * 1000000))
