def solution(s):


    s = list(s)

    close = []

    if s[-1] == '(':
        return False

    while s:
        cur = s.pop()
        if cur == ')':
            close.append(')')

        else:
            if len(close) > 0:
                close.pop()
            else:
                return False
    if close:
        return False

    return True

print(solution("()()"))