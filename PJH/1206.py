import sys

sys.stdin = open("input/1206_input.txt", "r")

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각w을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())

    buildings = list(map(int, input().split()))
    view = 0

    for i in range(N):
        left = False
        right = False

        if i == 0:
            left = True

        elif i == 1:
            if buildings[i - 1] < buildings[i]:
                left = True
        else:
            if buildings[i - 2] < buildings[i] and buildings[i - 1] < buildings[i]:
                left = True

        if i == N - 1:
            right = True
        elif i == N - 2:
            if buildings[i + 1] < buildings[i]:
                right = True
        else:
            if buildings[i + 2] < buildings[i] and buildings[i + 1] < buildings[i]:
                right = True

        if left and right:
            if i == 0:
                view += buildings[i] - max(buildings[i + 1 : i + 3])
            elif i == N - 1:
                view += buildings[i] - max(buildings[i - 2 : i + 1])
            else:
                view += buildings[i] - max(
                    max(buildings[i - 2 : i]), max(buildings[i + 1 : i + 3])
                )

    print(f"#{test_case} {view}")
