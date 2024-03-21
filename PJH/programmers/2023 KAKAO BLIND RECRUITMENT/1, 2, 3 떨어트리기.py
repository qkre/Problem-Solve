from collections import defaultdict, deque


def solution(edges, target):
    answer = []

    tree = defaultdict(list)
    for s, e in edges:
        tree[s].append(e)
    for i in tree.keys():
        tree[i].sort()

    min_visit, max_visit = create_min_max(target)
    node_visit, visit = create_node_visit(tree, min_visit, max_visit)
    if node_visit == [-1]:
        return [-1]
    node_nums = create_node_nums(target, node_visit)

    for node in visit:
        answer.append(node_nums[node].pop())

    print(answer)

    return answer


def create_min_max(target):
    min_visit = defaultdict(int)
    max_visit = defaultdict(int)

    for node, visit in enumerate(target, 1):
        max_visit[node] = visit

        quotient, remainder = divmod(visit, 3)
        if remainder:
            quotient += 1
        min_visit[node] = quotient

    return min_visit, max_visit


def create_node_visit(tree, min_visit, max_visit):
    node_child_index = defaultdict(int)
    node_visit = defaultdict(int)
    required_visit = sum(min_visit.values())
    visit = []
    while required_visit:
        parent = 1
        while tree[parent]:
            index = node_child_index[parent]
            child = tree[parent][index]
            index += 1

            if index == len(tree[parent]):
                index = 0

            node_child_index[parent] = index

            parent = child

        node_visit[parent] += 1
        visit.append(parent)
        if node_visit[parent] <= min_visit[parent]:
            required_visit -= 1

        elif max_visit[parent] < node_visit[parent]:
            return [-1], visit

    return node_visit, visit

def create_node_nums(target, node_visit):
    node_nums = defaultdict(list)
    for node, t in enumerate(target, 1):
        nums = []
        three, two = divmod(t - node_visit[node], 2)

        for _ in range(three):
            nums.append(3)
        if two:
            nums.append(2)

        while len(nums) < node_visit[node]:
            nums.append(1)

        node_nums[node] = nums

    return node_nums


solution([[2, 4], [1, 2], [6, 8], [1, 3], [5, 7], [2, 5], [3, 6], [6, 10], [6, 9]], [0, 0, 0, 3, 0, 0, 5, 1, 2, 3])
solution([[1, 2], [1, 3]], [0, 7, 3])
solution([[1, 3], [1, 2]], [0, 7, 1])
