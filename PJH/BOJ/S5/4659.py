from sys import stdin
from collections import deque

input = stdin.readline

def solution():
    mo = list("aeiou")
    za = [chr(i) for i in range(97, 123) if chr(i) not in mo]

    while True:
        password = input().rstrip()
        if password == 'end':
            break
        password_copy = password

        password = deque(list(password))
        is_mo = False
        is_valid = True
        stack = []
        while password:
            now = password.popleft()
            if now in mo:
                is_mo = True
            if not stack:
                stack.append(now)
            else:
                if len(stack) < 2:
                    if stack[-1] == now and now not in 'eo':
                        is_valid = False
                        break
                    elif stack[-1] in mo and now in za:
                        stack = [now]
                    elif stack[-1] in za and now in mo:
                        stack = [now]
                    else:
                        stack.append(now)
                else:
                    if stack[-1] == now and now not in 'eo':
                        is_valid = False
                        break
                    if now in mo:
                        if stack[-1] in mo and stack[-2] in mo:
                            is_valid = False
                            break
                        else:
                            stack = [now]
                    else:
                        if stack[-1] in za and stack[-2] in za:
                            is_valid = False
                            break
                        else:
                            stack = [now]
        if is_mo and is_valid:
            print(f"<{password_copy}> is acceptable.")
        else:
            print(f"<{password_copy}> is not acceptable.")


solution()