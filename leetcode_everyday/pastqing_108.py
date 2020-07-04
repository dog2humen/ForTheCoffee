# coding:utf8

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
	#return self.sortedArrayToBST_v1(nums)
	return self.sortedArrayToBST_v2(nums)
    def sortedArrayToBST_v1(self, nums: List[int]) -> TreeNode:
	'''
            recursive: bst中序遍历正好是有序数组, 所以直接从有序数组构造bst即可
            要求尽量平衡, 则选择数组中间为根节点, 递归左子树, 右子树也是如此即可
	'''

        return self.helper(0, len(nums) - 1, nums)
        

    def helper(self, left, right, nums):
        
        # terminated
        if left > right:
            return

        # current level
        mid = left + (right - left) // 2
        root = TreeNode(nums[mid])
        root.left = self.helper(left, mid - 1, nums)
        root.right = self.helper(mid + 1, right, nums)
        return root

    def sortedArrayToBST_v2(self, nums: List[int]) -> TreeNode:
        '''
            迭代dfs 使用栈
        '''
        if len(nums) == 0:
            return None
        
        res = TreeNode(0)
        stack = []
        left, right = 0, len(nums) - 1
        stack.append(right)
        stack.append(left)
        stack.append(res)

        while stack:
            root = stack.pop() # the TreeNode type
            left = stack.pop()
            right = stack.pop()
            mid = left + (right - left) // 2
            root.val = nums[mid]

            if left <= mid - 1:
                root.left = TreeNode(0)
                stack.append(mid - 1)
                stack.append(left)
                stack.append(root.left)
            
            if right >= mid + 1:
                root.right = TreeNode(0)
                stack.append(right)
                stack.append(mid + 1)
                stack.append(root.right)


        return res
