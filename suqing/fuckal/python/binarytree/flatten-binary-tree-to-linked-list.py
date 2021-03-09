# coding:utf8
"""
    114. 二叉树展开为链表
    给你二叉树的根结点 root ，请你将它展开为一个单链表：
    展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。
    展开后的单链表应该与二叉树 先序遍历 顺序相同。

    示例 1：
    输入：root = [1,2,5,3,4,null,6]
    输出：[1,null,2,null,3,null,4,null,5,null,6]

    链接：https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.flatten_v1(root)

    def flatten_v1(self, root: TreeNode) -> None:
        """
            递归思路
            1. 将root的左子树, 和右子树拉平
            2. 将右子树接到左子树后面
        """

        if not root:
            return None

        self.flatten_v1(root.left)
        self.flatten_v1(root.right)

        # 将左子树变为右子树
        left, right = root.left, root.right
        root.left = None
        root.right = left
        # 将原先的右子树接到左子树后面
        cur = root
        while cur.right:
            cur = cur.right

        cur.right = right

