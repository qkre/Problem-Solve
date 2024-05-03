from sys import stdin
input = stdin.readline
M = int(input())
S = 0

for _ in range(M):
    commands = list(input().split())
    x = 0
    if len(commands) == 2:
        cmd = commands[0]
        x = int(commands[1])
    else:
        cmd = commands[0]

    if cmd == 'add':
        S |= 1 << x
    elif cmd == 'remove':
        S &= ~(1 << x)
    elif cmd == 'check':
        if S & 1 << x:
            print(1)
        else:
            print(0)
    elif cmd == 'toggle':
        S = S ^ (1 << x)
    elif cmd == 'all':
        S = -1
    elif cmd == 'empty':
        S = 0

