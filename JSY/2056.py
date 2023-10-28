import sys

sys.stdin = open("input/2056_input.txt")

t = int(input())

for c in range(t):
    temp = ""

    date = input()

    for i in range(len(date)):
        if i == 4 or i == 6:
            temp += "/"
        temp += date[i]

    if int(temp[5]) > 2 or (int(temp[5]) == 0 and int(temp[6]) == 0):
        print(f"#{c+1} -1")

    elif int(temp[6]) == 2 and int(temp[8]) * 10 + int(temp[9]) > 28:
        print(f"#{c+1} -1")

    else:
        print(f"#{c+1} {temp}")
