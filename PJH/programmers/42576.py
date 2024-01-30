def solution(participant, completion):

    hash = {}

    for name in participant:
        if hash.get(name):
            hash[name] += 1
        else:
            hash[name] = 1

    for name in completion:
        hash[name] -= 1
        if hash[name] == 0:
            del hash[name]


    answer = list(hash)

    return answer[0]

solution(	["mislav","mislav","mislav","mislav"],	["mislav","mislav","mislav"])