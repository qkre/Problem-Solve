from bisect import bisect_right

def solution(people, limit):
    answer = 0

    people.sort()
    low, high = 0, len(people)-1

    while low < high:
        if people[low] + people[high] <= limit:
            low +=1
            high -= 1
        else:
            high -=1
        answer += 1

    if low == high:
        answer += 1


    return answer

print(solution( [10, 50, 100],160))