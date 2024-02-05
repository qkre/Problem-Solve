def solution(prices):
    answer = []


    for i in range(len(prices)):
        temp = 0
        passed = False
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                temp += 1

            else:
                passed = True
                break
        if passed:
            temp += 1
        answer.append(temp)


    return answer


print(solution([3, 4, 5, 1, 2, 1]))