# coding:utf8
"""
    2. 两数相加
    给你两个非空的链表，表示两个非负的整数。它们每位数字都是按照逆序的方式存储的
    并且每个节点只能存储一位数字。
    请你将两个数相加，并以相同形式返回一个表示和的链表。
    你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

    输入：l1 = [2,4,3], l2 = [5,6,4]
    输出：[7,0,8]
    解释：342 + 465 = 807.
    链接：https://leetcode-cn.com/problems/add-two-numbers
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
            2 -> 4 -> 3
          +                = 7 -> 0 -> 8
            5 -> 6 -> 4
        """
        head = ListNode(-1)
        cur = head
        carry = 0 # 表示进位
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            val = (x + y + carry) % 10
            cur.next = ListNode(val)
            carry = (x + y + carry) // 10
            cur = cur.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next


        if carry == 1:
            cur.next = ListNode(1)

        return head.next
