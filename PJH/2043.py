N, K = map(int, input().split())

cnt = 1
while K != N:
    cnt += 1
    K += 1
    if K == 1000:
        K = 0

print(cnt)
