import sys

sys.stdin = open("input/1244_input.txt", "r")


def dfs(index, count):
    global result
    if count == int(cnt):
        result = max(int("".join(data)), result)
        return
    for now in range(index, len(data)):
        for max_idx in range(now + 1, len(data)):
            if data[now] <= data[max_idx]:
                data[now], data[max_idx] = data[max_idx], data[now]
                dfs(now, count + 1)
                data[now], data[max_idx] = data[max_idx], data[now]

    if result == 0 and count < int(cnt):
        extra = (int(cnt) - count) % 2
        # 짝수라면 그대로, 홀수라면 한 번 변경
        if extra == 1:  # 홀수라면
            data[-1], data[-2] = data[-2], data[-1]
        dfs(index, int(cnt))


t = int(input())

for tc in range(1, t + 1):
    data, cnt = input().split()
    data = list(data)
    result = 0
    dfs(0, 0)

    print("#%d %d" % (tc, result))
