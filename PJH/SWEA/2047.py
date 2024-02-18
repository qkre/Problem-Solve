import os
import sys

current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"input/{current_file}_input.txt", "r")


title = list(input())

for i in range(len(title)):
    title[i] = title[i].upper()

result = ["".join(title)]

for _ in result:
    print(_)

output = open(f"output/{current_file}_output.txt", "r").readlines()
output = [line.strip() for line in output]
print(result == output)
