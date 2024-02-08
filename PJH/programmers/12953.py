

def solution(arr):
    import math

    while len(arr) > 1:
        A = arr[0]
        B = arr[1]

        arr = arr[2:]

        arr.append(A*B//math.gcd(A,B))

    return arr[-1]
solution([2, 6, 8, 14])