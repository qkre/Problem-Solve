from collections import deque


def solution(coin, cards):
    answer = 0

    n = len(cards)
    target = n + 1
    deck = cards[:n // 3]
    cards = deque(cards[n // 3:])
    picked = []

    while cards:
        answer += 1

        a, b = cards.popleft(), cards.popleft()

        picked.append(a)
        picked.append(b)

        is_possible = False

        for i in deck:
            if target - i in deck:
                deck.remove(i)
                deck.remove(target - i)
                is_possible = True
                break

        if is_possible:
            continue


        if coin >= 1:
            for i in deck:
                if target - i in picked:
                    deck.remove(i)
                    picked.remove(target - i)
                    is_possible = True
                    break

        if is_possible:
            coin -= 1
            continue

        if coin >= 2:
            for i in picked:
                if target - i in picked:
                    picked.remove(i)
                    picked.remove(target - i)
                    is_possible = True
                    break

            if is_possible:
                coin -= 2
                continue

        if not is_possible:
            break

    if is_possible:
        answer += 1
    print(answer)
    return answer


solution(4, [3, 6, 7, 2, 1, 10, 5, 9, 8, 12, 11, 4])
solution(3, [1, 2, 3, 4, 5, 8, 6, 7, 9, 10, 11, 12])
solution(2, [5, 8, 1, 2, 9, 4, 12, 11, 3, 10, 6, 7])
solution(10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])
solution(1, [6, 2, 1, 4, 5, 3])
solution(8, [1, 12, 2, 11, 3, 10, 4, 9, 5, 8, 6, 7])
