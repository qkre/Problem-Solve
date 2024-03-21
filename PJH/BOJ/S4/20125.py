N = int(input())
cookies = [list(input()) for _ in range(N)]

is_head = False
head = ()
heart = ()
left, right, waist, left_leg, right_leg = 0, 0, 0, 0, 0
for r in range(N):
    stack = []
    for c in range(N):
        if cookies[r][c] == '*':
            if not is_head:
                head = (r+1, c+1)
                is_head = True
            elif is_head:
                stack.append((r+1, c+1))
    if stack and not heart:
        for i in range(len(stack)):
            if stack[i][1] == head[1]:
                heart = stack[i]
            else:
                if not heart:
                    left += 1
                else:
                    right += 1

for c in range(N):
    stack = []
    for r in range(heart[0], N):
        if cookies[r][c] == '*':
            stack.append('*')

    if stack:
        if left_leg == 0:
            left_leg = len(stack)
        elif waist == 0:
            waist = len(stack)
        else:
            right_leg = len(stack)

print(*heart)
print(left, right, waist, left_leg, right_leg)