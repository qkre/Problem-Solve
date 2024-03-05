import sys
sys.setrecursionlimit(10**8)


class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self.__insert_value(self.root, data)
        return self.root is not None

    def __insert_value(self, node, data):
        if node is None:
            node = Node(data)
        else:
            if data <= node.data:
                node.left = self.__insert_value(node.left, data)
            else:
                node.right = self.__insert_value(node.right, data)

        return node

    def preorder(self, node):

        if node is None:
            return

        print(node.data)

        if node.left:
            self.preorder(node.left)
        if node.right:
            self.preorder(node.right)

    def postorder(self,node):

        if node is None:
            return

        if node.left:
            self.postorder(node.left)
        if node.right:
            self.postorder(node.right)

        print(node.data)

bst = BST()
while True:
    try:
        bst.insert(int(input()))
    except EOFError:
        break

bst.postorder(bst.root)