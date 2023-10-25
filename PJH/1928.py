import sys

sys.stdin = open("input/1928_input.txt", "r")


encoding_table = list(
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
)


T = int(input())

for case in range(1, T + 1):
    encoded = list(input())
    binary_encoded = []

    print(f"#{case} ", end="")

    for i in encoded:
        binary = format(encoding_table.index(i), "b")
        for i in list(binary.zfill(6)):
            binary_encoded.append(i)

    binary_decoded = []

    for i in range(0, len(binary_encoded), 8):
        decoded = "".join(binary_encoded[i : i + 8])
        decoded = "0b" + decoded
        binary_decoded.append(decoded)

    for binary in binary_decoded:
        ascii_code = int(binary, 2)
        print(chr(ascii_code), end="")

    print()
