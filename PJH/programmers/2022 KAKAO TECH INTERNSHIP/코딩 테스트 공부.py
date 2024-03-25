def solution(alp, cop, problems):
    answer = 0
    max_alp = max_cop = 0

    for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
        max_alp = max(max_alp, alp_req)
        max_cop = max(max_cop, cop_req)

    alp = min(alp, max_alp)
    cop = min(cop, max_cop)
    times = [[float('inf') for _ in range(max_cop + 1)] for _ in range(max_alp + 1)]

    times[alp][cop] = 0

    for a in range(alp, max_alp + 1):
        for c in range(cop, max_cop + 1):
            if a + 1 <= max_alp:
                times[a + 1][c] = min(times[a + 1][c], times[a][c] + 1)
            if c + 1 <= max_cop:
                times[a][c + 1] = min(times[a][c + 1], times[a][c] + 1)

            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if a >= alp_req and c >= cop_req:
                    na, nc = min(a + alp_rwd, max_alp), min(c + cop_rwd, max_cop)
                    times[na][nc] = min(times[na][nc],
                                        times[a][c] + cost)

    answer = times[max_alp][max_cop]
    return answer


solution(10, 10, [[10, 15, 2, 1, 2], [20, 20, 3, 3, 4]])
solution(0, 0, [[0, 0, 2, 1, 2], [4, 5, 3, 1, 2], [4, 11, 4, 0, 2], [10, 4, 0, 4, 2]])
