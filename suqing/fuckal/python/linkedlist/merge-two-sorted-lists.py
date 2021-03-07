# coding:utf8
"""
    21. 合并两个有序链表
    将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
    输入：l1 = [1,2,4], l2 = [1,3,4]
    输出：[1,1,2,3,4,4]
    https://leetcode-cn.com/problems/merge-two-sorted-lists/
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        #return self.mergeTwoLists_v1(l1, l2)
        return self.mergeTwoLists_v2(l1, l2)

    def mergeTwoLists_v1(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
            递归
        """
        if not l1 or not l2:
            return l1 or l2

        if l1.val < l2.val:
            l1.next  = self.mergeTwoLists_v1(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists_v1(l1, l2.next)
            return l2


    def mergeTwoLists_v2(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
            迭代做法
        """
        p1, p2, nhead = l1, l2, ListNode(-1)
        p = nhead
        while p1 and p2:
            if p1.val < p2.val:
                p.next = p1
                p1 = p1.next
            else:
                p.next = p2
                p2 = p2.next
            p = p.next

        p.next = p1 or p2
        return nhead.next
