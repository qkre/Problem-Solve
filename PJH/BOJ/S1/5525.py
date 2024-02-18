from sys import stdin

input = stdin.readline

N = int(input())
M = int(input())
S = input().rstrip()


def solution(N, M, S):
    answer = 0

    idx = 0
    count = 0

    while idx < len(S):
        if S[idx:idx+3] == 'IOI':
            count += 1
            idx += 2
            if count == N:
                answer += 1
                count -= 1
        else:
            idx += 1
            count = 0


    return answer


print(solution(N, M, S))
