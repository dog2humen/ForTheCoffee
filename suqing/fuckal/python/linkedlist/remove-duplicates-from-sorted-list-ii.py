# coding:utf8
"""
    82. 删除排序链表中的重复元素 II
    给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。

    示例 1:
    输入: 1->2->3->3->4->4->5
    输出: 1->2->5

    链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        return self.deleteDuplicates_v1(head)
    def deleteDuplicates_v1(self, head: ListNode) -> ListNode:
        """
            递归
        """
