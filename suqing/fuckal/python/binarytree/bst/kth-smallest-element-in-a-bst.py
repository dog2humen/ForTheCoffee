# coding:utf8
"""
    230. 二叉搜索树中第K小的元素
    给定一个二叉搜索树的根节点 root ，和一个整数 k ，
    请你设计一个算法查找其中第 k 个最小元素（从 1 开始计数）。
    输入：root = [3,1,4,null,2], k = 1
    输出：1
    https://leetcode-cn.com/problems/kth-smallest-element-in-a-bst/
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        #return self.kthSmallest_v1(root, k)
        return self.kthSmallest_v2(root, k)

    def kthSmallest_v1(self, root: TreeNode, k: int) -> int:
        """
            bst 中序比那里为升序
        """
        res = 0
        rank = 0
        def helper(root: TreeNode, k: int):
            if not root:
                return
            helper(root.left, k)
            rank += 1
            if k == rank:
                res = root.val
                return 

            helper(root.right, k)

        helper(root, k)
        return res

    def kthSmallest_v2(self, root: TreeNode, k: int) -> int:
        """
            迭代中序遍历
        """
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            k -= 1
            if k == 0:
                break
            root = root.right

        return root.val




