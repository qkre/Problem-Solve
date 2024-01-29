def solution(numer1, denom1, numer2, denom2):

    an = numer1 * denom2


    bn = numer2 * denom1


    answer = [an + bn, denom1*denom2]

    i = 2
    checked = False
    while True:
        if i > min(answer) + 1:
            if checked:
                i = 2
                checked = False
            else:
                return answer

        if answer[0] % i == 0 and answer[1] % i == 0:
            answer[0] //= i
            answer[1] //= i
            checked = True

        i += 1


print(solution(1, 999, 2, 999))