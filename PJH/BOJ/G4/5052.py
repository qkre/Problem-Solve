from collections import defaultdict

T = int(input())

for case in range(T):
    N = int(input())
    phone_book = list(input() for _ in range(N))
    header = defaultdict(bool)

    for number in phone_book:
        header[number] = True

    for number in phone_book:
        is_exist = False
        target = ""
        for i in list(number):
            target += i
            if target == number:
                break

            if header[target]:
                is_exist = True
                break

        if is_exist:
            break

    if is_exist:
        print("NO")
    else:
        print("YES")