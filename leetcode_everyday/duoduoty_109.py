# encoding=utf8
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
        if not head:
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
