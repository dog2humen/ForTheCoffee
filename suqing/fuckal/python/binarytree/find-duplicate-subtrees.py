# coding:utf8
"""
    652. 寻找重复的子树
    给定一棵二叉树，返回所有重复的子树。对于同一类的重复子树，你只需要返回其中任意一棵的根结点即可。
    两棵树重复是指它们具有相同的结构以及相同的结点值。

        1
       / \
      2   3
     /   / \
    4   2   4
       /
      4
下面是两个重复的子树：

      2
     /
    4
和
4

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        return self.findDuplicateSubtrees_v1(root)

    def findDuplicateSubtrees_v1(self, root: TreeNode) -> List[TreeNode]:

        """
            递归思路
        """
        if not root:
            return '#'

        left_str = self.findDuplicateSubtrees_v1(root.left)
        right_str = self.findDuplicateSubtrees_v1(root.right)
        subTree = left_str + ',' + right_str + ',' + str(root.val)
        return subTree



