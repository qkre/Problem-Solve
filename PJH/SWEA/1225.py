import os
import sys

current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"input/{current_file}_input.txt", "r")


from collections import deque

result = []


def cycle(cnt):
    head = arr.popleft()

    if head - cnt > 0:
        arr.append(head - cnt)
        return True
    else:
        arr.append(0)
        return False


for case in range(1, 11):
    N = int(input())
    arr = deque(map(int, input().split()))
    cnt = 1
    while cycle(cnt):
        cnt += 1
        if cnt == 6:
            cnt = 1

    result.append(f"#{case} {' '.join(map(str, arr))}")

for _ in result:
    print(_)

output = open(f"output/{current_file}_output.txt", "r").readlines()
output = [line.strip() for line in output]
print(result == output)
