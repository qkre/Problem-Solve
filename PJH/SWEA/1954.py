import os
import sys
from check_answer import check_answer

current_file = os.path.basename(__file__)[:-3]
sys.stdin = open(f"../input/{current_file}.txt", "r", encoding="utf-8-sig")

result = []
T = int(input())
for case in range(1, T + 1):
    ans = 0
    N = int(input())
    maps = [[0 for _ in range(N)] for _ in range(N)]
    r, c, d = 0, 0, "R"
    while ans < N ** 2:
        ans += 1
        maps[r][c] = ans

        if d == "R":
            if c + 1 < N and maps[r][c + 1] == 0:
                c += 1
            else:
                r += 1
                d = "D"
        elif d == "D":
            if r + 1 < N and maps[r + 1][c] == 0:
                r += 1
            else:
                c -= 1
                d = "L"
        elif d == "L":
            if c - 1 >= 0 and maps[r][c - 1] == 0:
                c -= 1
            else:
                r -= 1
                d = "U"
        elif d == "U":
            if r - 1 >= 0 and maps[r - 1][c] == 0:
                r -= 1
            else:
                c += 1
                d = "R"

    result.append(f"#{case}")
    for row in maps:
        result.append(' '.join(map(str, row)))

for r in result:
    print(r)

check_answer(current_file, result)
