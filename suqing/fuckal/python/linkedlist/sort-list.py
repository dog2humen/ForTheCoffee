# coding:utf8
"""
    148. 排序链表
    给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。
    输入：head = [4,2,1,3]
    输出：[1,2,3,4]
    https://leetcode-cn.com/problems/sort-list/
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        return self.sortList_v1(head)
    def sortList_v1(self, head: ListNode) -> ListNode:
        """
            归并排序
        """

        # current level
        mid = self.getMidNode(head)
        right = mid.next
        head1 = self.sortList_v1(head)
        head2 = self.sortList_v1(right)
        res = self.merge(head1, head2)
        return res

    def getMidNode(self, head: ListNode):
        """
            头结点为head的链表, 返回其中间节点
            4->2->1->3->5
        """
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def merge(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
            合并两个有序链表, 返回合并后的链表头结点
        """
        nhead = ListNode(-1)
        p1, p2, p = headA, headB, nhead
        while p1 and p2:
            if p1.val < p2.val:
                p.next = p1
                p1 = p1.next
            else:
                p.next = p2
                p2 = p2.next

            p = p.next

        if p1:
            p.next = p1
        if p2:
            p.next = p2
        return nhead.next


