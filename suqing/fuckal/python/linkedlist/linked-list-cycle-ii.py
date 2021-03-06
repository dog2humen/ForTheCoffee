# coding:utf8
"""
    142. 环形链表 II
    给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
    为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 
    如果 pos 是 -1，则在该链表中没有环。注意，pos 仅仅是用于标识环的情况，并不会作为参数传递到函数中。

    输入：head = [3,2,0,-4], pos = 1
    输出：返回索引为 1 的链表节点
    解释：链表中有一个环，其尾部连接到第二个节点。
    链接：https://leetcode-cn.com/problems/linked-list-cycle-ii
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        """
            快慢指针
            快慢指针第一次相遇, slow走了一个环的周长, fast走了两个环的周长
            非环部分的长度+环起点到相遇点之间的长度就是环的整数倍
            解法:
                快慢指针第一次相遇后, 将fast指针指向head, 然后fast 和slow按照统一速度走, 第二次相遇时指针的位置就是入口节点
        """

        slow, fast = head, head
        while True:
            if not (fast and fast.next):
                return None

            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break

        fast = head
        while fast != slow:
            slow = slow.next
            fast = fast.next

        return fast
