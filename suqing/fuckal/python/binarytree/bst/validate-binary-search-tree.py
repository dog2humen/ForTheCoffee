# coding:utf8
"""
    98. 验证二叉搜索树
    给定一个二叉树，判断其是否是一个有效的二叉搜索树。
    假设一个二叉搜索树具有如下特征：
    节点的左子树只包含小于当前节点的数。
    节点的右子树只包含大于当前节点的数。
    所有左子树和右子树自身必须也是二叉搜索树。

   输入:
    2
   / \
  1   3
输出: true 

    链接：https://leetcode-cn.com/problems/validate-binary-search-tree
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        #return self.isValidBST_v1(root)
        return self.isValidBST_v2(root)
    def isValidBST_v1(self, root: TreeNode) -> bool:
        """
            递归
        """
        def helper(root: TreeNode, maxTree: TreeNode, minTree: TreeNode) -> bool:
            """
                以root为根节点的bst, 必须满足min.val < root.val < max.val
            """
            if not root:
                return True
            if maxTree and root.val >= maxTree.val:
                return False
            if minTree and root.val <= minTree.val:
                return False

            return helper(root.left, root, minTree) and helper(root.right, maxTree, root)
        
        return helper(root, None, None)

    def isValidBST_v2(self, root: TreeNode) -> bool:
        """
            中序遍历, 记录前驱节点
        """
        stack = []
        pre = None
        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            if pre and pre.val >= root.val:
                return False
            pre = root
            root = root.right
        return True

