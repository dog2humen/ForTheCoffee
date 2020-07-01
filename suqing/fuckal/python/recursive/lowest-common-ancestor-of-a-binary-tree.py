# coding:utf8
# 236 https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.lowestCommonAncestor_v1(root, p, q)
    
    def lowestCommonAncestor_v1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
            找到从root分别到p, q的路径, 从两个路径中寻找公共祖先
        """
        def helper(node, target, curPaths, res):
            if not node:
                return
            if node == target:
                curPaths.append(node)
                res.extend(curPaths[:])
                return
            helper(node.left, target, curPaths + [node], res)
            helper(node.right, target, curPaths + [node], res)

        paths_p, paths_q = [], []
        helper(root, p, [], paths_p)
        helper(root, q, [], paths_q)

        # 找公共祖先
        # [3, 5, 2, 4] [5, 2, 4]
        size_p, size_q = len(paths_p), len(paths_q)
        i, j = 0, 0
        res = None
        while i < size_p and j < size_q:
            if paths_p[i] == pathss_q[j]:
                res = paths_p[i]
            i += 1
            j += 1
        return res


    def lowestCommonAncestor_v2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pass
    
