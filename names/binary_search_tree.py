from collections import deque


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BSTNode(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)

    def contains(self, target):
        if target == self.value:
            return True
        elif target > self.value:
            if self.right:
                return self.right.contains(target)
        elif target < self.value:
            if self.left:
                return self.left.contains(target)
        else:
            return False

    def get_max(self):
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    def for_each(self, fn):
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):
        node = self.value

        if self.left:
            self.left.in_order_print(node)
        print(node)
        if self.right:
            self.right.in_order_print(node)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self, node=None):
        # breadth-first-traversal
        node = deque()
        node.append(self)
        while len(node) > 0:
            current = node.popleft()
            print(current.value)
            if current.left:
                node.append(current.left)
            if current.right:
                node.append(current.right)
    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    def dft_print(self, node):
        node = []
        node.append(self)
        while len(node) > 0:
            current = node.pop()
            print(current.value)
            if current.right:
                node.append(current.right)
            if current.left:
                node.append(current.left)
