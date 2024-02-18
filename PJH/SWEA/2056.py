import sys

sys.stdin = open("input/2056_input.txt", "r")

T = int(input())

for case in range(1, T + 1):
    date = list(input())

    year = int("".join(date[:4]))
    month = int("".join(date[4:6]))
    day = int("".join(date[6:]))

    if 0 < month <= 12:
        if month == 2:
            if 0 < day <= 28:
                print(
                    f"#{case} {''.join(date[:4])}/{''.join(date[4:6])}/{''.join(date[6:])}"
                )
            else:
                print(f"#{case} -1")

        elif month in [1, 3, 5, 7, 8, 10, 12]:
            if 0 < day <= 31:
                print(
                    f"#{case} {''.join(date[:4])}/{''.join(date[4:6])}/{''.join(date[6:])}"
                )
            else:
                print(f"#{case} -1")
        else:
            if 0 < day <= 30:
                print(
                    f"#{case} {''.join(date[:4])}/{''.join(date[4:6])}/{''.join(date[6:])}"
                )
            else:
                print(f"#{case} -1")

    else:
        print(f"#{case} -1")
