# coding:utf8
"""
    83. 删除排序链表中的重复元素
    给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
    示例 1:
    输入: 1->1->2
    输出: 1->2
    https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        #return self.deleteDuplicates_v1(head)
        return self.deleteDuplicates_v2(head)

    def deleteDuplicates_v1(self, head: ListNode) -> ListNode:
        """
            递归
        """
        if not head:
            return head
        cur = head
        while cur and cur.val == head.val:
            cur = cur.next
        head.next = self.deleteDuplicates_v1(cur)
        return head
    def deleteDuplicates_v2(self, head: ListNode) -> ListNode:
        """
            迭代做法
            1->1->1->2
        """
        pre, cur = None, head
        while cur:
            tmp = cur
            while tmp.next:
                if tmp.next.val == cur.val:
                    tmp.next = tmp.next.next
                else:
                    tmp = tmp.next
            cur = cur.next
        return head


