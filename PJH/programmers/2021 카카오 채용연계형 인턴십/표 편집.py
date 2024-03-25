class Node:
    def __init__(self):
        self.removed = False
        self.prev = None
        self.next = None

def solution(n, k, cmd):
    answer = ''

    node_arr = [Node() for _ in range(n)]

    for i in range(1, n):
        node_arr[i].prev = node_arr[i-1]
        node_arr[i-1].next = node_arr[i]

    curr = node_arr[k]
    stack = []

    for cmd_str in cmd:
        cmd_list = list(cmd_str.split())
        command = cmd_list[0]
        number = 0
        if len(cmd_list) > 1:
            number = int(cmd_list[1])

        if command == 'D':
            moved = 0
            while moved < number:
                moved += 1
                curr = curr.next

        elif command == 'U':
            moved = 0
            while moved < number:
                moved += 1
                curr = curr.prev

        elif command == 'C':
            stack.append(curr)
            curr.removed = True

            prev = curr.prev
            next = curr.next

            if prev:
                curr.prev.next = next
            if next:
                curr.next.prev = prev
                curr = next
            else:
                curr = prev

        elif command == 'Z':
            r = stack.pop()
            r.removed = False
            prev = r.prev
            next = r.next

            if prev:
                r.prev.next = r
            if next:
                r.next.prev = r

    for i in range(n):
        if node_arr[i].removed:
            answer += 'X'
        else:
            answer += 'O'

    print(answer)


    return answer