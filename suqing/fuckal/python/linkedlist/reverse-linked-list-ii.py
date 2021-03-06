# coding:utf8
"""
    92. 反转链表 II
    反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
    说明:
    1 ≤ m ≤ n ≤ 链表长度。
    示例:
    输入: 1->2->3->4->5->NULL, m = 2, n = 4
    输出: 1->4->3->2->5->NULL
    链接：https://leetcode-cn.com/problems/reverse-linked-list-ii
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        #return self.reverseBetween_v1(head, left, right)
        return self.reverseBetween_v2(head, left, right)

    def reverseBetween_v1(self, head: ListNode, left: int, right: int) -> ListNode:
        """
            递归
            left == 1 相当于翻转前right个结点
        """
        if left == 1:
            return self.reverseN(head, right)

        head.next = self.reverseBetween_v1(head.next, left - 1, right - 1)
        return head

    def reverseBetween_v2(self, head: ListNode, left: int, right: int) -> ListNode:
        """
            迭代
            1.找到第m个位置, 第n个位置
            2.翻转[m, n] 返回头结点和尾节点
        """

        i = 1
        pre, cur = None, head
        rpre, rhead = None, None # 记录m对应的节点的指针以及m的前驱
        rtail = None # 记录n对应节点的指针

        while i <= right and cur:
            if i == left:
                rpre = pre
                rhead = cur
            if i == right:
                rtail = cur

            pre = cur
            cur = cur.next
            i += 1
                
        rnext = cur # n节点的后继 
        nhead, ntail = self.reverseHT(rhead, rtail)
        ntail.next = rnext

        if rpre:
            rpre.next = nhead
        else:
            return nhead

        return head

    def reverseHT(self, head: ListNode, tail: ListNode) -> ListNode:
        """
            翻转从head -> tail的链表
            返回新的头结点以及尾结点的指针
        """
        pre, cur = None, head
        while cur != tail:
            nextNode = cur.next
            cur.next = pre
            pre = cur
            cur = nextNode

        cur.next = pre
        return cur, head



    def reverseN(self, head: ListNode, n: int) -> ListNode:
        """
            翻转头结点为head的前n个节点
            返回翻转后的头结点
        """
        if n == 1:
            self.nextNode = head.next
            return head

        last = self.reverseN(head.next, n - 1)
        head.next.next = head
        head.next = self.nextNode
        return last



