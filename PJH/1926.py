import sys

sys.stdin = open("input/1926_input.txt", "r")

N = int(input())

arr = []

for i in range(1, N + 1):
    if "3" in list(str(i)) or "6" in list(str(i)) or "9" in list(str(i)):
        cnt = 0
        cnt += list(str(i)).count("3")
        cnt += list(str(i)).count("6")
        cnt += list(str(i)).count("9")

        arr.append("-" * cnt)

    else:
        arr.append(i)

print(*arr)
