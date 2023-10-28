import sys

sys.stdin = open("input/1989_input.txt")

t = int(input())

for c in range(t):
    word = input()

    for i in range(len(word)):
        if word[i] != word[i - i - 1 - i]:
            print(f"#{c+1} 0")
            break
    else:
        print(f"#{c+1} 1")
