def solution(clothes):
    import itertools

    answer = 1

    clothes_table = {}

    for (item, clothes_type) in clothes:
        if clothes_table.get(clothes_type):
            clothes_table.get(clothes_type).append(item)
        else:
            clothes_table[clothes_type] = [item]

    clothes_type = list(clothes_table.keys())

    for key in clothes_type:
        answer *= (len(clothes_table[key]) + 1)

    answer -= 1

    return answer


solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])
