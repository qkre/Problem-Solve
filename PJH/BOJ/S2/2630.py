white, blue = 0, 0

def solution(N, arr):
    global white, blue
    checked = [[False for _ in range(N)] for _ in range(N)]
    cut(N, arr, checked, 0, 0)
    print(white)
    print(blue)

    return

def cut(N, arr, checked, sx, sy):
    global white, blue

    valid = True
    if N > 1:
        target = arr[sy][sx]
        for y in range(sy, sy + N):
            for x in range(sx, sx + N):
                if arr[y][x] != target:
                    valid = False
                    break
            if not valid:
                break

    if valid:
        if arr[sy][sx] == 0:
            white += 1
        else:
            blue += 1
        for y in range(sy, sy+N):
            for x in range(sx, sx + N):
                checked[y][x] = True

    else:
        for y in range(sy, sy+N, N//2):
            for x in range(sx, sx+N, N//2):
                cut(N//2, arr, checked, x, y)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

solution(N, arr)