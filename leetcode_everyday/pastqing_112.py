# coding:utf8
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        #return self.hasPathSum_v1(root, sum)
        return self.hasPathSum_v2(root, sum)
    
    def hasPathSum_v1(self, root: TreeNode, sum: int) -> bool:
        '''
            dfs 递归
        '''
        if not root:
            return False

        return self.helper(root, sum)
    
    def helper(self, root, target):
        # terminated
        if root is None:
            return False 
        if root.left is None and root.right is None:
            return root.val == target

        # cur level
        
        return self.helper(root.left, target - root.val) or self.helper(root.right, target - root.val)


    def hasPathSum_v2(self, root: TreeNode, sum: int) -> bool:
        '''
            dfs 迭代
        '''
        if not root:
            return False
        stack = [(root, root.val)]
        target = sum
        while stack:
            node, curSum = stack.pop()
            if node.left is None and node.right is None:
                if curSum == target:
                    return True

            if node.right:
                stack.append((node.right, curSum + node.right.val))
            if node.left:
                stack.append((node.left, curSum + node.left.val))


        return False
