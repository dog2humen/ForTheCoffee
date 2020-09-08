# coding:utf8
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from typing import List
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        return self.levelOrderBottom_v1(root)
    def levelOrderBottom_v1(self, root: TreeNode) -> List[List[int]]:
        queue = [root] if root else []
        res = []

        while queue:
            size = len(queue)
            tmp = []
            for node in range(size):
                cur = queue.pop(0)
                tmp.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

            res.insert(0, tmp[:])

        return res





