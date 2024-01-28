def solution(dots):
    answer = 0

    comb = [[(0, 1), (2, 3)], [(0, 2), (1, 3)], [(0, 3), (1, 2)]]

    for c in comb:
        a = c[0]
        b = c[1]

        am = (dots[a[1]][1] - dots[a[0]][1]) / (dots[a[1]][0] - dots[a[0]][0])
        bm = (dots[b[1]][1] - dots[b[0]][1]) / (dots[b[1]][0] - dots[b[0]][0])

        if am == bm:

            ac = dots[a[0]][1] - am * dots[a[0]][0]
            bc = dots[b[0]][1] - bm * dots[b[0]][0]

            if ac == bc:
                if (dots[a[0]][0] < dots[b[0]][0]
                        and dots[a[1]][0] > dots[b[1]][0]
                        and dots[a[0]][1] < dots[b[0]][1]
                        and dots[a[1]][1] > dots[
                            b[1]][1]):
                    answer = 1
                    break
                if (dots[b[0]][0] < dots[a[0]][0]
                        and dots[b[1]][0] > dots[a[1]][0]
                        and dots[b[0]][1] < dots[a[0]][1]
                        and dots[b[1]][1] > dots[a[1]][1]):
                    answer = 1
                    break
            else:
                answer = 1

    return answer


print(solution([[1, 1], [2, 2], [3, 3], [4, 4]]))
