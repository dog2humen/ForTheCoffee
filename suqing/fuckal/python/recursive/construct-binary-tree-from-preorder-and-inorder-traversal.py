# coding:utf8
# 105 https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
	return self.buildTree_v1(preorder, inorder)

    def buildTree_v1(self, preorder: List[int], inorder: List[int]) -> TreeNode:
	"""
            先序的第一个是根, 从先序的根去中序中划分左右子树	
            前序遍历 preorder = [3,9,20,15,7]
            中序遍历 inorder = [9,3,15,20,7]
	"""
        root = TreeNode(preorder[0])
        idx = inorder.index(root.val)
        root.left = self.buildTree_v1(preorder[1 : idx + 1], inorder[:idx]) 
        root.right = self.buildTree_v1(preorder[idx + 1:], inorder[idx + 1:])
        return root


