# coding:utf8

class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right



def preorder(root, res = None):
    if not root:
        return []
    if not res:
        res = []

    res.append(root.val)
    preorder(root.left, res)
    preorder(root.right, res)

    return res


def preorder_iter(root):
    res = []
    stack = [root] if root else []
    while stack:
        root = stack.pop()
        res.append(root.val)
        if root.right:
            stack.append(root.right)
        if root.left:
            stack.append(root.left)

    return res



