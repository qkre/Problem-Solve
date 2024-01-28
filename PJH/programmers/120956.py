def solution(babbling):
    pronounce = ["aya", "ye", "woo", "ma"]

    answer = 0


    for babb in babbling:

        list_babb = list(babb)

        temp = ''

        say = False

        for i in list_babb:
            temp += i
            if temp in pronounce:
                say = True
                temp = ''

        if temp != '':
            say = False

        if say:
            answer += 1

    return answer

print(solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]))