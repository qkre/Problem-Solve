from itertools import permutations
from collections import deque
import re


def solution(expression):
    answer = 0

    expression = re.split('([-+*])', expression)

    priorities = list(permutations(list("+-*"), 3))

    for priority in priorities:
        exp = expression.copy()
        for op in priority:

            while op in exp:
                op_idx = exp.index(op)
                A = exp[op_idx - 1]
                B = exp[op_idx + 1]
                C = str(eval(A + op + B))

                exp = exp[:op_idx - 1] + [C] + exp[op_idx + 2:]
        answer = max(answer, abs(int(exp[0])))

    print(answer)
    return answer

solution("100-200*300-500+20")
