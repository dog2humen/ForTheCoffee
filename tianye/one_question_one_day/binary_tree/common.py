# encoding=utf8

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    """
        110. 平衡二叉树
        给定一个二叉树，判断它是否是高度平衡的二叉树。

        本题中，一棵高度平衡二叉树定义为：

        一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。

        示例 1:

        给定二叉树 [3,9,20,null,null,15,7]

            3
           / \
          9  20
            /  \
           15   7
        返回 true 。

        示例 2:

        给定二叉树 [1,2,2,3,3,null,null,4,4]

               1
              / \
             2   2
            / \
           3   3
          / \
         4   4
        返回 false 。
    """
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isBalanced_v2(root)

    # 自顶向下
    def isBalanced_v1(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return abs(self.height(root.left) - self.height(root.right)) <= 1 and \
            self.isBalanced_v1(root.left) and self.isBalanced_v1(root.right)

    def height(self, root):
        if not root:
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1

    # 自底向上 还需理解
    def isBalanced_v2(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.dfs(root) != -1

    def dfs(self, root):
        if not root: return 0
        left = self.dfs(root.left)
        if left == -1: return -1
        right = self.dfs(root.right)
        if right == -1: return -1
        return max(left, right) + 1 if abs(left - right) < 2 else -1
    
    
    """
        109. 有序链表转换二叉搜索树
        给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。

        本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

        示例:

        给定的有序链表： [-10, -3, 0, 5, 9],

        一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：

              0
             / \
           -3   9
           /   /
         -10  5
    """
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        return self.sortedListToBST_v1(head)

    #  快慢指针
    def sortedListToBST_v1(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        i
            return None
        slow, fast, pre = head, head, None

        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next

        root = TreeNode(slow.val)

        if pre:
            pre.next = None
            root.left = self.sortedListToBST_v1(head)

        root.right = self.sortedListToBST_v1(slow.next)

        return root


    # 转化成有序数组，找中间节点
    def sortedListToBST_v2(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        return self.build_BST(arr, 0, len(arr) - 1)

    def build_BST(self, arr, start, end):
        if start > end:
            return None
        mid = start + (end - start) // 2
        root = TreeNode(arr[mid])
        root.left = self.build_BST(arr, start, mid - 1)
        root.right = self.build_BST(arr, mid + 1, end)
        return root


    """
    111. 二叉树的最小深度
        给定一个二叉树，找出其最小深度。

        最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

        说明: 叶子节点是指没有子节点的节点。

        示例:

        给定二叉树 [3,9,20,null,null,15,7],

            3
           / \
          9  20
            /  \
           15   7
        返回它的最小深度  2.
    """
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.minDepth_v1(root)

    # dfs
    def minDepth_v1(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        if not root.left and not root.right:
            return 1

        l = self.minDepth(root.left)
        r = self.minDepth(root.right)

        if not root.left or not root.right:
            return l + r + 1

        return min(l, r) + 1

    # bfs
    def minDepth_v2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        import collections
        queue = collections.deque([(root, 1)])
        while queue:
            node, depth = queue.popleft()
            if not node.left and not node.right:
                return depth
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))

        return 0
