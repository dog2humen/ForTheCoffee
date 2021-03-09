# coding:utf8
"""
    116. 填充每个节点的下一个右侧节点指针
    给定一个 完美二叉树 ，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：

给定一个 完美二叉树 ，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
初始状态下，所有 next 指针都被设置为 NULL。

输入：root = [1,2,3,4,5,6,7]
输出：[1,#,2,3,#,4,5,6,7,#]
解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。序列化的输出按层序遍历排列，同一层节点由 next 指针连接，'#' 标志着每一层的结束。

链接：https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        return self.connect_v1(root)
    def connect_v1(self, root: 'Node') -> 'Node':
        """
            递归思路
        """
        def connect(node1, node2):
            if not node1 or not node2:
                return None
            
            node1.next = node2
            # 相同根节点
            connect(node1.left, node1.right)
            connect(node2.left, node2.right)
            # 不同根节点
            connect(node1.right, node2.left)

        if not root:
            return None
        connect(root.left, root.right)
        return root


