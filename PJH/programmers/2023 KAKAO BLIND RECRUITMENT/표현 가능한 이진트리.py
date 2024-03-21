def solution(numbers):
    answer = []

    for number in numbers:
        binary = get_full_binary(number)
        result = check(binary, False)
        if not result:
            answer.append(0)
        else:
            answer.append(1)

    print(answer)
    return answer


def check(binary, dummy):
    if len(binary) == 1:
        return not dummy or binary == '0'

    root_idx = len(binary) // 2
    root = binary[root_idx]

    if dummy and root == '1':
        return False

    dummy = dummy or root == '0'

    return check(binary[:root_idx], dummy) and check(binary[root_idx + 1:], dummy)


def get_full_binary(number):
    binary = bin(number)[2:]

    level, child = 0, 1

    while child < len(binary):
        level += 1
        child += 2 ** level

    return '0' * (child - len(binary)) + binary


solution([8, 9, 10, 42, 58, 64, 127, 128, 129])
