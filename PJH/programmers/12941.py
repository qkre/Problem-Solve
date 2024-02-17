def solution(A, B):
    answer = 0

    A.sort()
    B.sort()

    while A:
        answer += A.pop(0)*B.pop()

    return answer