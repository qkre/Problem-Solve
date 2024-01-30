def solution(phone_book):
    answer = True

    phone_book.sort()

    used = {}

    for number in phone_book:
        used[number] = 1

    for number in phone_book:
        for i in range(1, len(number)):
            if used.get(number[:i]) == 1:
                return False

    return answer

solution(["119", "97674223", "1195524421"])