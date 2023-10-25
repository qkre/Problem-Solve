import sys

sys.stdin = open("input/1928_input.txt", "r")


encoding_table = list(
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
)


T = int(input())

for case in range(1, T + 1):
    encoded = list(input())

    for i in encoded:
        binary = format(encoding_table.index(i), "b")
        print(binary)
