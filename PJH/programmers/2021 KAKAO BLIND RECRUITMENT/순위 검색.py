from bisect import bisect_left
def solution(info, query):
    answer = []

    users = []

    anything = [[[[], [], []] for _ in range(3)] for _ in range(3)]
    cpp = [[[[], [], []] for _ in range(3)] for _ in range(3)]
    java = [[[[], [], []] for _ in range(3)] for _ in range(3)]
    python = [[[[], [], []] for _ in range(3)] for _ in range(3)]

    for s in info:
        lang, work, level, like, score = s.split()
        score = int(score)
        if work == 'backend':
            work = 1
        else:
            work = 2

        if level == 'junior':
            level = 1
        else:
            level = 2

        if like == 'chicken':
            like = 1
        else:
            like = 2

        for w in [0, work]:
            for l in [0, level]:
                for f in [0, like]:
                    anything[w][l][f].append(score)

        if lang == 'cpp':
            for w in [0, work]:
                for l in [0, level]:
                    for f in [0, like]:
                        cpp[w][l][f].append(score)
        elif lang == 'java':
            for w in [0, work]:
                for l in [0, level]:
                    for f in [0, like]:
                        java[w][l][f].append(score)
        else:
            for w in [0, work]:
                for l in [0, level]:
                    for f in [0, like]:
                        python[w][l][f].append(score)


    for i in range(3):
        for j in range(3):
            for k in range(3):
                anything[i][j][k].sort()
                java[i][j][k].sort()
                cpp[i][j][k].sort()
                python[i][j][k].sort()

    for q in query:
        lang, _, work, _, level, _, like, score = q.split(" ")
        score = int(score)
        passed = 0
        if work =='-':
            work = 0
        elif work == 'backend':
            work = 1
        else:
            work = 2

        if level == '-':
            level = 0
        elif level == 'junior':
            level = 1
        else:
            level = 2

        if like == '-':
            like = 0
        elif like == 'chicken':
            like = 1
        else:
            like = 2

        if lang == '-':
            passed = len(anything[work][level][like]) - bisect_left(anything[work][level][like], score)
        elif lang == 'java':
            passed = len(java[work][level][like]) - bisect_left(java[work][level][like], score)
        elif lang == 'cpp':
            passed = len(cpp[work][level][like]) - bisect_left(cpp[work][level][like], score)
        elif lang == 'python':
            passed = len(python[work][level][like]) - bisect_left(python[work][level][like], score)

        answer.append(passed)

    print(answer)

    return answer

