# coding:utf8
"""
    105. 从前序与中序遍历序列构造二叉树
    根据一棵树的前序遍历与中序遍历构造二叉树。
    注意:
    你可以假设树中没有重复的元素。
    例如，给出
    前序遍历 preorder = [3,9,20,15,7]
    中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7

    链接：https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
	return self.buildTree_v1(preorder, inorder)

    def buildTree_v1(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        def helper(preorder: List[int], pStart: int, pEnd: int, inorder: List[int], iStart: int, iEnd: int) -> TreeNode:

            if pStart > pEnd:
                return None

            root_val = preorder[pStart]
            root = TreeNode(root_val)

            index = 0
            for i in range(iStart, iEnd + 1):
                if inorder[i] == root_val:
                    index = i
                    break

            left_size = index - iStart
            root.left = helper(preorder, pStart + 1, pStart + left_size, inorder, iStart, index - 1)
            root.right = helper(preorder, pStart + left_size + 1, pEnd, inorder, index + 1, iEnd)

            return root

        return helper(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)
	
