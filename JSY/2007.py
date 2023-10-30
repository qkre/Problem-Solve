import sys

sys.stdin = open("input/2007_input.txt")

t = int(input())

for c in range(1, t + 1):
    arr = input()
    temp = "".join(arr[0])
    cnt = 0
    for i in range(1, len(arr)):
        if temp[0] == arr[i] and temp[1] == arr[i + 1]:
            break
        else:
            temp += arr[i]

    print(f"#{c} {len(temp)}")
# 테케 오류 아래 주석 처럼 푸는게 맞는거 같다
# for i in range(0, len(arr), len(temp)):
#     if arr[i : i + len(temp) - 1] == temp:
#         cnt += 1

# print(f"#{c} {cnt}")
