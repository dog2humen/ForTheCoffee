# coding:utf8
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from typing import List
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        return self.bfs(root)

    def bfs(self, node):

        queue = [node] if node else []
        res = []
        while queue:
            size = len(queue)
            avg = 0
            for _ in range(size):
                cur = queue.pop(0)
                avg += cur.val
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            
            res.append(avg/size)

        return res

