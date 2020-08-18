# coding:utf8
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        return self.inorderTraversal_v1(root)
    def inorderTraversal_v1(self, root: TreeNode) -> List[int]:
        """ dfs use stack """
        stack, res, node = [], [], root

        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            
            cur = node.pop()
            res.append(cur.val)
            node = cur.right
