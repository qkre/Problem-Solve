from sys import stdin

input = stdin.readline

def solution():
    N, game = input().split()
    players = list(input().rstrip() for _ in range(int(N)))
    players = list(set(players))
    answer = 0
    if game == 'Y':
        answer = len(players)
    elif game == 'F':
        answer = len(players) // 2
    elif game == 'O':
        answer = len(players) // 3

    print(answer)

solution()