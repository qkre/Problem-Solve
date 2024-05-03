import sys
from collections import deque, defaultdict

input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))
target = sorted(arr)
q = deque()
checked = defaultdict(bool)
visited = []
q.append((arr, 0,))

max_cnt = 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1

while q:
    arr, cnt = q.popleft()

    if cnt > max_cnt:
        break

    if arr == target:
        print(cnt)
        quit()

    for i in range((N - K) + 1):
        new_arr = arr[:i]
        new_arr += reversed(arr[i:i + K])
        new_arr += arr[i + K:]
        # if not checked[''.join(map(str, new_arr))]:
        #     checked[''.join(map(str,new_arr))] = True
        #     q.append((new_arr, cnt + 1))
        if ''.join(map(str, new_arr)) not in visited:
            visited.append(''.join(map(str, new_arr)))
            q.append((new_arr, cnt + 1))

print(-1)
