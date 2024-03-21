from collections import defaultdict


def solution(commands):
    answer = []

    excel = [['' for _ in range(51)] for _ in range(51)]
    pointer = defaultdict(list)

    for i in range(51):
        for j in range(51):
            pointer[(i, j)] = [(i, j)]

    while commands:
        C = list(commands.pop(0).split())

        if C[0] == 'UPDATE':
            if len(C) == 4:
                r, c, value = int(C[1]), int(C[2]), C[3]
                update_pointer(r, c, value, pointer, excel)
            else:
                value1, value2 = C[1], C[2]
                update_value(value1, value2, excel)

        elif C[0] == 'MERGE':
            r1, c1, r2, c2 = map(int, C[1:])
            merge_pointer(r1, c1, r2, c2, pointer, excel)

        elif C[0] == 'UNMERGE':
            r, c = map(int, C[1:])
            unmerge_pointer(r, c, pointer, excel)


        elif C[0] == 'PRINT':
            r, c = map(int, C[1:])
            if excel[r][c] == '':
                answer.append('EMPTY')
            else:
                answer.append(excel[r][c])

    print(answer)

    return answer


def update_pointer(r, c, value, pointer, excel):
    for r, c in pointer[(r, c)]:
        excel[r][c] = value


def update_value(value1, value2, excel):
    for r in range(51):
        for c in range(51):
            if excel[r][c] == value1:
                excel[r][c] = value2


def merge_pointer(r1, c1, r2, c2, pointer, excel):
    if excel[r1][c1] != '':
        pointer[(r1, c1)] = list(set(pointer[(r1, c1)] + pointer[(r2, c2)]))
        for r, c in pointer[(r1, c1)]:
            pointer[(r, c)] = pointer[(r1, c1)]
            excel[r][c] = excel[r1][c1]

    else:
        pointer[(r2, c2)] = list(set(pointer[(r1, c1)] + pointer[(r2, c2)]))
        for r, c in pointer[(r2, c2)]:
            pointer[(r, c)] = pointer[(r2, c2)]
            excel[r][c] = excel[r2][c2]


def unmerge_pointer(r, c, pointer, excel):
    merged = pointer[(r, c)]
    value = excel[r][c]
    for rr, cc in merged:
        pointer[(rr, cc)] = [(rr, cc)]
        excel[rr][cc] = ''

    excel[r][c] = value


solution(["UPDATE 1 1 안녕", "MERGE 1 1 2 2", "MERGE 3 3 2 2", "PRINT 3 3", "PRINT 1 1"])
