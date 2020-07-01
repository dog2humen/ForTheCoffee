# coding:utf8
# 98 https://leetcode-cn.com/problems/validate-binary-search-tree/

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        #return self.isValidBST_v1(root)
        return self.isValidBST_v2(root)
    def isValidBST_v1(self, root: TreeNode) -> bool:
        '''
            递归
        '''
        self.pre = float('-inf')
        return self.helper(root)
    
    def helper(self, node):
        if node:
            res = self.helper(node.left)
            if not res:
                return False
            if node.val <= self.pre:
                return False
            self.pre = node.val
            return self.helper(node.right)
        return True

    def isValidBST_v2(self, root: TreeNode) -> bool:
        '''
            迭代, 根据bst中序遍历的单调递增
        '''
        stack = []
        preVal = float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            cur = stack.pop()
            if cur.val <= preVal:
                return False
            preVal = cur.val
            root = cur.right
        return True
            
