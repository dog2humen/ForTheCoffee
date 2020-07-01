# coding:utf
# 144 https://leetcode-cn.com/problems/binary-tree-preorder-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        #return self.preorderTraversal_v1(root)
        return self.preorderTraversal_v2(root)
    def preorderTraversal_v1(self, root: TreeNode) -> List[int]:
        '''
            递归dfs
        '''
        res = []
        self.helper(root, res)
        return res

    def helper(self, node, res):
        if node:
            res.append(node.val)
            self.helper(node.left, res)
            self.helper(node.right, res)

    def preorderTraversal_v2(self, root: TreeNode) -> List[int]:
        '''
            迭代dfs
        '''
        stack = [root] if root else []
        res = []
        while stack:
            cur = stack.pop()
            if cur:
                res.append(cur.val)
                stack.append(cur.right)
                stack.append(cur.left)
        return res

