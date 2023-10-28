import os
import sys
import copy

current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"input/{current_file}_input.txt", "r")
result = []

T = int(input())

for case in range(1, T + 1):

    N, M = map(int, input().split())

    
    

for _ in result:
    print(_)

output = open(f"input/{current_file}_output.txt", "r").readlines()
output = [line.strip() for line in output]
print(result == output)
