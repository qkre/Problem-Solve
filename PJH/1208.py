import sys

sys.stdin = open("input/1208_input.txt", "r")

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    boxes = list(map(int, input().split()))

    for i in range(N):
        top_index = boxes.index(max(boxes))
        bottom_index = boxes.index(min(boxes))

        boxes[top_index] -= 1
        boxes[bottom_index] += 1

    ans = max(boxes) - min(boxes)

    print(f"#{test_case} {ans}")
