import sys

sys.stdin = open("input/2001_input.txt")

t = int(input())

# n = n*n 배열
# m = m*m 파리채 크기
for i in range(t):
    n, m = map(int, input().split())

    table = [list(map(int, input().split())) for _ in range(n)]
    cnt = []
    for j in range(n - m + 1):
        for k in range(n - m + 1):
            temp = 0
            for a in range(m):
                for b in range(m):
                    temp += table[j + a][k + b]

            cnt.append(temp)
    print(f"#{i+1} {max(cnt)}")
