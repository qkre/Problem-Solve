def solution(n, tops):
    answer = 0

    dp_a = [0 for _ in range(n+1)]
    dp_b = [0 for _ in range(n+1)]

    dp_a[1] = 1
    if tops[0] == 1:
        dp_b[1] = 3
    else:
        dp_b[1] = 2

    for i in range(2, n+1):
        if tops[i - 1] == 1:
            dp_a[i] = (dp_a[i - 1] + dp_b[i - 1]) % 10007
            dp_b[i] = (dp_a[i - 1] * 2 + dp_b[i - 1] * 3) % 10007
        else:
            dp_a[i] = (dp_a[i - 1] + dp_b[i - 1]) % 10007
            dp_b[i] = (dp_a[i - 1] + dp_b[i - 1] * 2) % 10007

    answer = dp_a[-1] + dp_b[-1]
    print(answer)
    return answer


solution(4, [1, 1, 0, 1])
solution(2, [0, 1])
solution(10, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
