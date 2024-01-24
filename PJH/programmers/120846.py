def solution(n):

    prime = [True for _ in range(n+1)]
    mid = int(n**0.5)

    for i in range(2, mid + 1):
        if prime[i]:
            for j in range(i*2, n+1, i):
                prime[j] = False



    answer = prime.count(False)

    return answer

solution(15)