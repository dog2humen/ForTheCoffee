# coding:utf8
"""
    234. 回文链表
    判断一个链表是否为回文链表。
    示例 1:
    输入: 1->2
    输出: false
    https://leetcode-cn.com/problems/palindrome-linked-list/
"""
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        return self.isPalindrome_v1(head)
    def isPalindrome_v1(self, head: ListNode) -> bool:
        """
            1->2->2->1
            1. find mid
            2. 翻转
            3. 比较两部分
        """
        if not head:
            return True

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 若是奇数, slow在中间, fast在结尾
        # 若是偶数, fast为none, slow需要再进一步
        if fast:
            slow = slow.next

        # 从slow翻转
        right = self.reverse(slow)
        left = head
        # 比较
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True


    def reverse(self, head: ListNode) -> ListNode:

        pre, cur = None, head
        while cur:
            nextNode = cur.next
            cur.next = pre
            pre = cur
            cur = nextNode
        return pre



    def isPalindrome_v2(self, head: ListNode) -> bool:
        """
            不破坏链表结构
        """

