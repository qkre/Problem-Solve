def solution(brown, yellow):

    width = 3
    height = 3

    while True:
        width = height
        checked = False

        if width * 2 + (height - 2) * 2 == brown:
            if (width - 2) * (height - 2) == yellow:
                break


        while width * 2 + (height - 2) * 2 <= brown:
            width += 1

            if width * 2 + (height - 2) * 2 == brown:
                if (width-2) * (height - 2) == yellow:
                    checked = True
                    break

        if checked:
            break


        height += 1


    answer = [width, height]

    return answer


solution(24, 24)
