import sys

sys.stdin = open("input/1989_input.txt", "r")

T = int(input())
result = []
for case in range(1, T + 1):
    word = list(input())
    reversed_word = list(reversed(word))

    if word == reversed_word:
        result.append(f"#{case} 1")
    else:
        result.append(f"#{case} 0")

for _ in result:
    print(_)

output = open("output/1989_output.txt", "r").readlines()
output = [line.strip() for line in output]
print(result == output)
