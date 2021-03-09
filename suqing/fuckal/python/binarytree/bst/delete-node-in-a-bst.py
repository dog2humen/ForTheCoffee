# coding:utf8
"""
    450. 删除二叉搜索树中的节点
    给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key 对应的节点，并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。
    一般来说，删除节点可分为两个步骤：
    首先找到需要删除的节点；
    如果找到了，删除它。
    说明： 要求算法时间复杂度为 O(h)，h 为树的高度。

root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 / \   \
2   4   7

    5
   / \
  4   6
 /     \
2       7

    5
   / \
  2   6
   \   \
    4   7

    链接：https://leetcode-cn.com/problems/delete-node-in-a-bst
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        return self.deleteNode_v1(root, key)		

    def deleteNode_v1(self, root: TreeNode, key: int) -> TreeNode:
        """
            二分查找
        """
        if not root:
            return None

        if root.val > key:
            root.left = self.deleteNode_v1(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode_v1(root.right, key)
        else:
            # 叶子节点
            # 只有一个孩子节点
            # 有两个孩子, 左子树的最大或者右子树的最小 
            if root.left:
                left_right_most = root.left
                while left_right_most.right:
                    left_right_most = left_right_most.right
                left_right_most.right = root.right
                return root.left
            else:
                return root.right

        return root

