import sys

sys.stdin = open("input/1983_input.txt")
score = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]

t = int(input())

for c in range(t):
    n, k = map(int, input().split())
    rank = []
    for i in range(n):
        mid, final, work = map(int, input().split())
        mid *= 35
        final *= 45
        work *= 20
        rank.append(mid + final + work)

    # 키값이 k 인 놈의 idx 찾기
    k_score = rank[k - 1]
    rank.sort(reverse=True)

    value = n // 10
    ret = rank.index(k_score) // value

    print(f"#{c+1} {score[ret]}")
