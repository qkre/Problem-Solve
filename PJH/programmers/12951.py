def solution(s):
    s = s.split(" ")
    for i in range(len(s)):
        s[i] = s[i].capitalize()

    answer = ' '.join(s)

    return answer

print(solution("3people a2UnFollowed me 123"))