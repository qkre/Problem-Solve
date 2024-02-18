
answer = -1
def solution(k, dungeons):
    global answer
    length = len(dungeons)

    def dfs(cnt, k, visited):
        global answer
        if cnt == length:
            answer = cnt
            return cnt

        answer = max(answer, cnt)

        for i in range(length):
            if visited[i]:
                continue

            if dungeons[i][0] > k:
                continue
            visited[i] = True
            dfs(cnt+1, k-dungeons[i][1], visited)
            visited[i] = False

        return cnt

    for i in range(length):
        dungeon = dungeons[i]
        if k < dungeon[0]:
            continue
        visited = [False for _ in range(length)]
        dfs(0, k, visited)

    return answer

solution(80,	[[80,20],[50,40],[30,10]])