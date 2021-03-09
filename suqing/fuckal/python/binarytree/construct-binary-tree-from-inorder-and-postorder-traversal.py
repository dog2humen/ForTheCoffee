# coding:utf8
"""
    106. 从中序与后序遍历序列构造二叉树
    根据一棵树的中序遍历与后序遍历构造二叉树。

    注意:
    你可以假设树中没有重复的元素。

    例如，给出

    中序遍历 inorder = [9,3,15,20,7]
    后序遍历 postorder = [9,15,7,20,3]
    返回如下的二叉树：
    3
   / \
  9  20
    /  \
   15   7

    链接：https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        return self.buildTree_v1(inorder, postorder)
    def buildTree_v1(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        """
            后续遍历最后一个元素为根
        """
        
        def helper(inorder, iStart, iEnd, postorder, pStart, pEnd):
            if iStart > iEnd:
                return None

            root_val = postorder[pEnd]
            index = 0
            for i in range(iStart, iEnd + 1):
                if inorder[i] == root_val:
                    index = i
                    break

            left_size = index - iStart

            root = TreeNode(root_val)
            root.left = helper(inorder, iStart, index - 1, postorder, pStart, pStart + left_size - 1)
            root.right = helper(inorder, index + 1, iEnd, postorder, pStart + left_size, pEnd - 1)
            return root
        
        return helper(inorder, 0, len(inorder) - 1, postorder, 0, len(postorder) - 1)
