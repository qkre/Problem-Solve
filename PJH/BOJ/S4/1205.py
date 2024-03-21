N, T, P = map(int, input().split())
scores = list(map(int, input().split()))
scores.sort()
rank = 1
ranks = [[] for _ in range(P + 1)]

while scores:
    now = scores.pop()
    ranks[rank].append(now)
    while True and scores:
        if scores[-1] == now:
            ranks[rank].append(scores.pop())
        else:
            break
    rank += len(ranks[rank])

answer = -1

for i in range(1, P+1):
    if T in ranks[i]:
        answer = i
        break

print(answer)