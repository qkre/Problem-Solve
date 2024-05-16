from collections import defaultdict

N = int(input())


def is_ok(S):
    for i in range(1, len(S) // 2 + 1):
        A = S[len(S) - i:]
        B = S[len(S) - 2 * i: len(S) - i]
        if A == B:
            return False
    return True

def permutation(depth, now):
    if depth == N:
        print("".join(now))
        quit()

    for i in "123":
        if now:
            if is_ok(now + [i]):
                permutation(depth + 1, now + [i])
        else:
            permutation(depth + 1, [i])


checked = defaultdict(bool)
permutation(0, [])
