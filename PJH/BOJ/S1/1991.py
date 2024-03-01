from sys import stdin
input = stdin.readline

def preorder(Tree, data):

    print(data, end='')

    if Tree[data][0] != '.':
        preorder(Tree, Tree[data][0])

    if Tree[data][1] != '.':
        preorder(Tree, Tree[data][1])

    return

def inorder(Tree, data):
    if Tree[data][0] != '.':
        inorder(Tree, Tree[data][0])

    print(data, end='')

    if Tree[data][1] != '.':
        inorder(Tree, Tree[data][1])

    return

def postorder(Tree, data):
    if Tree[data][0] != '.':
        postorder(Tree, Tree[data][0])

    if Tree[data][1] != '.':
        postorder(Tree, Tree[data][1])

    print(data, end='')

    return


def solution(N):

    Tree = {}

    for i in range(N):
        root, left, right = input().split()
        Tree[root] = [left, right]


    preorder(Tree, 'A')
    print()
    inorder(Tree, 'A')
    print()
    postorder(Tree, 'A')




solution(int(input()))