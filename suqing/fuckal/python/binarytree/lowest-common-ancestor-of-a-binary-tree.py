# coding:utf8
"""
    236. 二叉树的最近公共祖先
    给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

    百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

    输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
    输出：3
    解释：节点 5 和节点 1 的最近公共祖先是节点 3 。

    链接：https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree
"""
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

        if not root:
            return None
        if root == p or root == q:
            return root

        left = self.lowestCommonAncestor_v1(root.left, p, q)
        right = self.lowestCommonAncestor_v1(root.right, p, q)

        if left and right:
            return root

        if left is None and right is None:
            return None

        return left or right

                    
