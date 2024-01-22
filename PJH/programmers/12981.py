def solution(n, words):
    answer = [0, 0]

    for i in range(len(words) - 1):
        prev = list(words[i])
        next = list(words[i+1])
        history = words[:i+1]

        if prev[-1] != next[0]:
            answer = [(i+1) % n + 1, (i+1) // n + 1]
            break

        if ''.join(next) in history:
            answer = [(i+1) % n + 1, (i+1) // n + 1]
            break

    return answer

n = 3
words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]

print(solution(n, words))