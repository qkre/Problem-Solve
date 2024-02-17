def solution(s):
    cnt = 0
    zeros = 0
    while True:
        cnt += 1
        zeros += s.count("0")
        s = '1' * s.count('1')

        if s == '1':
            break

        s = format(len(s), 'b')
    answer = [cnt, zeros]
    return answer

solution("0111010")