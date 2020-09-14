# coding:utf8
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from typimg import List

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        #return self.inorderTraversal_v1(root)
        return self.inorderTraversal_v2(root)
	
    def inorderTraversal_v1(self, root: TreeNode) -> List[int]:
        """ dfs recursive"""
        res = []
        self.dfs(root, res)
        return res

    def dfs(self, node, res):
        if node:
            self.dfs(node.left)
            res.append(node.val)
            self.dfs(node.right)

    def inorderTraversal_v2(self, root: TreeNode) -> List[int]:
        """ dfs iter """
        stack, res = [], []

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            cur = stack.pop()
            res.append(cur.val)
            root = cur.right

        return res



