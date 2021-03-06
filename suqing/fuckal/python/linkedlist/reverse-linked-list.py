# coding: utf8
"""
    206. 反转链表
    反转一个单链表。
    示例:
    输入: 1->2->3->4->5->NULL
    输出: 5->4->3->2->1->NULL
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        #return self.reverseList_v1(head)
        return self.reverseList_v2(head)

    def reverseList_v1(self, head: ListNode) -> ListNode:
        """
            递归解法
        """
        def helper(h: ListNode) -> ListNode:
            """
                返回翻转之后的头结点
            """
            if h.next is None:
                return h
            last = helper(h.next)
            h.next.next = h
            h.next = None
            return last
        
        if not head:
            return None

        return helper(head)

    def reverseList_v2(self, head: ListNode) -> ListNode:
        """
            迭代, 头插法
        """
        pre, cur = None, head
        while cur:
            nextNode = cur.next
            cur.next = pre
            pre = cur
            cur = nextNode

        return pre
    
