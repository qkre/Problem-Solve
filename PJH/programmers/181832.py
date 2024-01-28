def solution(n):
    answer = [[0 for _ in range(n)] for _ in range(n)]
    direction = 0

    x, y = 0, 0
    for i in range(1, n ** 2 + 1):
        answer[y][x] = i

        while True and i < n**2:
            if direction == 0:
                if n > x+1 >= 0 and answer[y][x+1] == 0:
                    x += 1
                    break

                else:
                    direction += 1



            if direction == 1:
                if n > y+1 >= 0 and answer[y+1][x] == 0:
                    y += 1
                    break

                else:
                    direction += 1



            if direction == 2:
                if n > x-1 >= 0 and answer[y][x-1] == 0:
                    x -= 1
                    break

                else:
                    direction += 1

            if direction == 3:
                if n > y-1 >= 0 and answer[y-1][x] == 0:
                    y -= 1
                    break

                else:
                    direction = 0


    return answer


print(solution(4))
