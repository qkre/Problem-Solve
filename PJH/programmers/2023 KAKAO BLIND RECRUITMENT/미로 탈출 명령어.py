from heapq import heappop, heappush
from copy import deepcopy


def solution(n, m, y, x, r, c, k):
    answer = ''

    maps = [[' ' for _ in range(m + 1)] for _ in range(n + 1)]

    maps[y][x] = 'S'
    maps[r][c] = 'E'

    distance = abs(y - r) + abs(x - c)
    if distance > k:
        print('impossible')
        return 'impossible'
    if (k - distance) % 2 != 0:
        print('impossible')
        return 'impossible'

    # dlru
    down = max(r - y, 0)
    left = max(x - c, 0)
    right = max(c - x, 0)
    up = max(y - r, 0)
    pair = (k - distance) // 2

    for _ in range(k):
        if (down or pair) and y < n:
            answer += 'd'
            if down:
                down -= 1
            else:
                pair -= 1
                up += 1

            y += 1

        elif (left or pair) and x > 1:
            answer += 'l'
            if left:
                left -= 1
            else:
                pair -= 1
                right += 1

            x -= 1

        elif (right or pair) and x < m:
            answer += 'r'
            if right:
                right -= 1
            else:
                pair -= 1
                left += 1

            x += 1
        else:
            answer += 'u'
            if up:
                up -= 1
            else:
                pair -= 1
                down += 1

            y -= 1

    print(answer)

    return answer


solution(3, 4, 2, 3, 3, 1, 5)
solution(2, 2, 1, 1, 2, 2, 2)
solution(3, 3, 1, 2, 3, 3, 4)
