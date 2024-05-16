N = int(input())
switches = ["-"] + list(map(int, input().split()))
M = int(input())

for _ in range(M):
    gender, number = map(int, input().split())

    if gender == 1:
        for i in range(number, N + 1, number):
            switches[i] = (switches[i] + 1) % 2
    else:
        idx = 0
        while True:
            left = number - (idx + 1)
            right = number + (idx + 1)

            if left < 1 or right > N:
                break

            if switches[left] != switches[right]:
                break

            idx += 1

        for i in range(number - idx, number + idx + 1):
            switches[i] = (switches[i] + 1) % 2

for i in range(1, N+1):
    print(switches[i], end=" ")
    if i % 20 == 0:
        print()