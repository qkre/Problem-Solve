import sys

sys.stdin = open("input/1289_input.txt", "r")

T = int(input())
result = []
for case in range(1, T + 1):
    memory = list(input())
    beginnig = ["0"] * len(memory)

    cnt = 0

    for i in range(len(memory)):
        if memory[i] != beginnig[i]:
            cnt += 1
            beginnig[i:] = memory[i] * len(beginnig[i:])
    
    result.append(f"#{case} {cnt}")

for _ in result:
    print(_)

output = open("output/1289_output.txt", "r").readlines()
output = [line.strip() for line in output]
print(result == output)
