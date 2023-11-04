import sys

sys.stdin = open("./input/1940_input.txt")

t = int(input())

for c in range(t):
    n = int(input())
    speed = 0
    distance = 0
    command = []

    for i in range(n):
        command = list(map(int, input().split()))

        if command[0] == 1:
            speed += command[1]
            distance += speed

        elif command[0] == 2:
            if speed < command[1]:
                speed = 0
            else:
                speed -= command[1]
            distance += speed

        elif command[0] == 0:
            distance += speed

    print(f"#{c+1} {distance}")
