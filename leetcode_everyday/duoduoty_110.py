# encoding=utf8
"""
110. 平衡二叉树
给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：

一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。

示例 1:

给定二叉树 [3,9,20,null,null,15,7]

    3
   / \
  9  20
    /  \
   15   7
返回 true 。

示例 2:

给定二叉树 [1,2,2,3,3,null,null,4,4]

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
返回 false 。
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isBalanced_v2(root)

    # 自顶向下
    def isBalanced_v1(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return abs(self.height(root.left) - self.height(root.right)) <= 1 and \
            self.isBalanced_v1(root.left) and self.isBalanced_v1(root.right)

    def height(self, root):
        if not root:
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1

    # 自底向上 还需理解
    def isBalanced_v2(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.dfs(root) != -1

    def dfs(self, root):
        if not root: return 0
        left = self.dfs(root.left)
        if left == -1: return -1
        right = self.dfs(root.right)
        if right == -1: return -1
        return max(left, right) + 1 if abs(left - right) < 2 else -1

