import sys

sys.stdin = open("input/1244_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    numbers, cnt = input().split()
    numbers = list(numbers)
    cnt = int(cnt)

    if numbers == sorted(numbers, reverse=True):
        for i in range(cnt):
            tmp = numbers[-2]
            numbers[-2] = numbers[-1]
            numbers[-1] = tmp
    else:
        swapped = 0
        index = 0

        reverse_sorted_numbers = sorted(numbers, reverse=True)

        while swapped != cnt:
            if numbers[index] < max(numbers[index + 1 :]):
                tmp = numbers[index]
                reversed_numbers = list(reversed(numbers[index + 1 :]))

                max_idx = (
                    len(numbers) - 1 - reversed_numbers.index(max(numbers[index + 1 :]))
                )

                numbers[index] = numbers[max_idx]
                numbers[max_idx] = tmp
                swapped += 1
                index += 1

            elif numbers == reverse_sorted_numbers:
                for j in range(index, cnt):
                    tmp = numbers[-2]
                    numbers[-2] = numbers[-1]
                    numbers[-1] = tmp
                    swapped += 1
                    if swapped == cnt:
                        break
            else:
                index += 1

    print(f"#{test_case} {''.join(numbers)}")

# 아무래도 뒤에서 부터 스왑 하는 것이 정답일 듯 .....
