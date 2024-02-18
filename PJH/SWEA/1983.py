import sys

sys.stdin = open("input/1983_input.txt", "r")

T = int(input())
result = []
for case in range(1, T + 1):
    N, K = map(int, input().split())

    each_scores = list(list(map(int, input().split())) for _ in range(N))

    scores = []

    for i in each_scores:
        scores.append(i[0] * 0.35 + i[1] * 0.45 + i[2] * 0.2)

    ranked = list(sorted(scores, reverse=True))

    K_rank = ranked.index(scores[K - 1]) + 1

    if K_rank <= N * 0.1:
        K_rank = "A+"
    elif K_rank <= N * 0.2:
        K_rank = "A0"
    elif K_rank <= N * 0.3:
        K_rank = "A-"
    elif K_rank <= N * 0.4:
        K_rank = "B+"
    elif K_rank <= N * 0.5:
        K_rank = "B0"
    elif K_rank <= N * 0.6:
        K_rank = "B-"
    elif K_rank <= N * 0.7:
        K_rank = "C+"
    elif K_rank <= N * 0.8:
        K_rank = "C0"
    elif K_rank <= N * 0.9:
        K_rank = "C-"
    else:
        K_rank = "D0"

    result.append(f"#{case} {K_rank}")

for _ in result:
    print(_)

output = open("output/1983_output.txt", "r").readlines()
output = [line.strip() for line in output]
print(result == output)
