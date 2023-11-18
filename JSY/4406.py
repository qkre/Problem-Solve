import sys
sys.stdin = open("C:/Users/jsio2/Computer/Algo/SWEA/input/4406_input.txt")
t = int(input())

arr = ["a", "e", "i", "o", "u"]

for c in range(t):
    word = input()

    for i in arr:
        if i in word:
            word = word.replace(i, "")

    print(f"#{c+1} {word}")
