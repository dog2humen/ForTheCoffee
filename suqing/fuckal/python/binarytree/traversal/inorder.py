# coding:utf8

class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right



def inorder(root, res = None):
    if not root:
        return []
    if not res:
        res = []

    inorder(root.left, res)
    res.append(root.val)
    inorder(root.right, res)
    return res


def inorder_iter(root):
    res, res = [], []
    while root or stack:
        while root:
            stack.append(root)
            root = root.left

        root = stack.pop()
        res.append(root.val)
        root = root.right

    return res



