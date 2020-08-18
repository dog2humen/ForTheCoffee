# coding:utf8
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        return self.sortedListToBST_v1(head)
    def sortedListToBST_v1(self, head: ListNode) -> TreeNode:
        return self.helper(head, None)

    def helper(self, head, tail):
        
        if head == tail:
            return None
        midNode = self.find_link_mid(head, tail)
        root = TreeNode(midNode.val)
        root.left = self.helper(head, midNode)
        root.right = self.helper(midNode.next, tail)

        return root
    
    def find_link_mid(self, head, tail):
        fast, slow = head.next, head
        pre = None
        while fast != tail and fast.next != tail:
            fast = fast.next.next
            pre = slow
            slow = slow.next

        return slow

	

