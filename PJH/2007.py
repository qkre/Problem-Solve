import sys

sys.stdin = open("input/2007_input.txt", "r")

T = int(input())
result = []
for case in range(1, T + 1):
    string = list(input())

    checked = True

    for i in range(1, len(string) + 1):
        if string[:i] == string[i : i * 2]:
            result.append(f"#{case} {i}")
            break


for _ in result:
    print(_)

output = open("output/2007_output.txt", "r").readlines()
output = [line.strip() for line in output]
print(result == output)
