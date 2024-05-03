import sys
input = sys.stdin.readline
from copy import deepcopy

di, dj = [-1, 1, 0, 0, 0], [0, 0, 0, -1, 1]
result = 101
arr = [[False] * 10 for _ in range(10)]
for i in range(10):
    a = input()
    for j in range(10):
        if a[j] == 'O':
            arr[i][j] = True

# 첫 줄의 모든 경우의 수
for ck in range(1 << 10):
    new_arr = deepcopy(arr)
    cnt = 0
    # 첫줄에 10개 전구 하나씩 탐색
    for k in range(10):
        # j번째 스위치를 누른다면 +1
        if ck & (1 << k):
            cnt += 1
            # 맨윗줄 방향 살피기
            for d in range(5):
                ni, nj = 0+di[d], k + dj[d]
                if 0<=ni<=9 and 0 <= nj <= 9:
                    new_arr[ni][nj] = not new_arr[ni][nj]


    for i in range(1,10):
        for j in range(10):
            if new_arr[i-1][j] == True:
                cnt += 1
                for d in range(5):
                    ni, nj = i + di[d], j + dj[d]
                    if 0 <= ni <= 9 and 0 <= nj <= 9:
                        new_arr[ni][nj] = not new_arr[ni][nj]

    if all(c == False for c in new_arr[-1]):
        result = min(result, cnt)
print(result if result < 101 else -1)