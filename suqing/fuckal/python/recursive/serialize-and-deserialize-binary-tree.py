# coding:utf8
# 297 https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        def helper(node):
            if node:
                res.append(str(node.val))
                helper(node.left)
                helper(node.right)
            else:
                res.append('none')

        helper(root)
        return ','.join(res)

	
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        input = iter(data.split(','))
        def helper():
            val = next(input)
            if val == 'none':
                return None
            node = TreeNode(val)
            node.left = helper()
            node.right = helper()
            return node
        return helper()

        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
