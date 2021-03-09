# coding:utf8

class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right



def postorder(root, res = None):
    if not root:
        return []
    if not res:
        res = []

    inorder(root.left, res)
    inorder(root.right, res)
    res.append(root.val)
    return res


def postorder_iter(root):
    stack = [root] if root else []
    tmp, res = [], []
    while stack:
        root = stack.pop()
        tmp.append(root.val)
        if root.left:
            stack.append(root.left)
        if root.right:
            stack.append(root.right)
    
    while tmp:
        res.append(tmp.pop())
    return res




