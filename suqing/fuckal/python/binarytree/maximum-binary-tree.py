# coding:utf8
"""
    654. 最大二叉树
    给定一个不含重复元素的整数数组 nums 。一个以此数组直接递归构建的 最大二叉树 定义如下：
    二叉树的根是数组 nums 中的最大元素。
    左子树是通过数组中 最大值左边部分 递归构造出的最大二叉树。
    右子树是通过数组中 最大值右边部分 递归构造出的最大二叉树。
    返回有给定数组 nums 构建的 最大二叉树 。

    链接：https://leetcode-cn.com/problems/maximum-binary-tree
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        return self.constructMaximumBinaryTree_v1(nums)

    def constructMaximumBinaryTree_v1(self, nums: List[int]) -> TreeNode:
        """
            递归思路:
            找到nums中的最大值, 构造根
            将数组分割为两个部分, 构造左子树和右子树
        """
        def helper(nums: List[int], left: int, right: int) -> TreeNode:
            if left > right:
                return None
            
            maxVal = float('-inf')
            nextCur = -1
            for i in range(left, right + 1):
                if maxVal < nums[i]:
                    maxVal = nums[i]
                    nextCur = i

            root = TreeNode(maxVal)
            root.left = helper(nums, left, nextCur - 1)
            root.right = helper(nums, nextCur + 1, right)

            return root

        return helper(nums, 0, len(nums) - 1)
