import re
def solution(new_id):
    answer = new_id

    # step 1.
    answer = answer.lower()

    # step 2.
    answer = ''.join(re.findall('[\w.-]', answer))

    # step 3.
    answer = ''.join(re.sub('\.{2,}', '.', answer))

    # step 4.
    if answer:
        if answer[0] == '.':
            if len(answer) > 1:
                answer = answer[1:]
            else:
                answer = ''
    if answer:
        if answer[-1] == '.':
            if len(answer) > 1:
                answer = answer[:-1]
            else:
                answer = ''

    # step 5.
    if not answer:
        answer = 'a'

    # step 6.
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]

    # step 7
    while len(answer) < 3:
        answer += answer[-1]

    print(answer)
    return answer

solution("...!@BaT#*..y.abcdefghijklm")
solution("z-+.^.")
solution("=.=")