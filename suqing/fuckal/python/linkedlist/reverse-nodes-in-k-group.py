# coding:utf8
"""
    25. K 个一组翻转链表
    给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
    k 是一个正整数，它的值小于或等于链表的长度。
    如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

    输入：head = [1,2,3,4,5], k = 2
    输出：[2,1,4,3,5]

    链接：https://leetcode-cn.com/problems/reverse-nodes-in-k-group
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        return self.reverseKGroup_v1(head, k)

    def reverseKGroup_v1(self, head: ListNode, k: int) -> ListNode:
        """
            递归思路, 每k个翻转一次
        """
        if not head:
            return None

        a, b = head, head # 区间[a, b)中包含k个待翻转的
        for i in range(k):
            if not b: # 不足k个, 不用翻转
                return head 
            b = b.next

        nhead = self.reverseHT(a, b)
        a.next = self.reverseKGroup_v1(b, k)
        return nhead

    def reverseHT(self, head, tail):
        """
            翻转区间为[head, tail)的链表
            返回翻转后的头结点
        """
        pre, cur = None, head
        while cur != tail:

            nextNode = cur.next
            cur.next = pre
            pre = cur
            cur = nextNode

        return pre
            
    def reverseKGroup_v2(self, head: ListNode, k: int) -> ListNode:
        """
            迭代
        """
