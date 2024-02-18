import sys

sys.stdin = open("input/5215_input.txt", "r")

T = int(input())
result = []


def dfs(depth, kcal, cur_score):
    global N, max_kcal, score

    if kcal > max_kcal or depth == N:
        return

    score = max(score, cur_score)

    for i in range(depth + 1, N):
        dfs(i, kcal + foods[i][1], cur_score + foods[i][0])


for case in range(1, T + 1):
    N, max_kcal = map(int, input().split())

    score = 0

    foods = list(list(map(int, input().split())) for _ in range(N))

    for i in range(N):
        dfs(i, foods[i][1], foods[i][0])

    result.append(f"#{case} {score}")


for _ in result:
    print(_)


output = open("output/5215_output.txt", "r").readlines()
output = [line.strip() for line in output]
print(result == output)
