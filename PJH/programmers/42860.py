def solution(name):
    answer = 0
    alpha = [chr(65 + i) for i in range(26)]
    state = ['A' for _ in range(len(name))]
    name = list(name)

    cursor = 0

    while state != name:

        target = name[cursor]

        if state[cursor] == target or answer == 0:

            left_move, right_move = 1, 1

            for left in range(cursor-1, -1 * len(name), -1):
                if state[left] != name[left]:
                    break
                left_move += 1

            for right in range(cursor+1, len(name)):
                if state[right] != name[right]:
                    break
                right_move += 1

            answer += min(left_move, right_move)
            if left_move < right_move:
                cursor -= left_move
            elif right_move < left_move:
                cursor += right_move
            else:
                left_count, right_count = 0, 0

                for left in range(cursor-1, -1 * len(name), -1):
                    if name[left] == 'A':
                        break
                    left_count += 1

                for right in range(cursor + 1, len(name)):
                    if name[right] == 'A':
                        break
                    right_count += 1

                if left_count > right_count:
                    cursor -= left_move
                else:
                    cursor += right_count

            continue

        up, down = 0, 0
        for up in range(26):
            if alpha[up] == target:
                break

        for down in range(-1, -27, -1):
            if alpha[down] == target:
                break
        down = abs(down)

        answer += min(up, down)
        state[cursor] = target

    return answer

solution("JEROEN")
