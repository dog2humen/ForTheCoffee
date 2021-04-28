# coding:utf8
"""
    503. 下一个更大元素 II
    给定一个循环数组（最后一个元素的下一个元素是数组的第一个元素），输出每个元素的下一个更大元素。数字 x 的下一个更大的元素是按数组遍历顺序，这个数字之后的第一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。如果不存在，则输出 -1。
输入: [1,2,1]
输出: [2,-1,2]
解释: 第一个 1 的下一个更大的数是 2；
数字 2 找不到下一个更大的数； 
第二个 1 的下一个最大的数需要循环搜索，结果也是 2。
链接：https://leetcode-cn.com/problems/next-greater-element-ii
"""

from typing import List
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        return self.nextGreaterElements_v1(nums)

    def nextGreaterElements_v1(self, nums: List[int]) -> List[int]:
        """
            单调栈思路
            复制一份数据作为输入解决环形数组的问题
        """
        size = len(nums)
        stack, res = [], [-1] * size
        for i in range(size * 2 - 1, -1, -1):
            while stack and nums[i % size] >= stack[-1]:
                stack.pop()

            res[i % size] = stack[-1] if stack else -1
            stack.append(nums[i % size])

        return res

if __name__ == '__main__':
    nums = [1, 2, 1]
    obj = Solution()
    print(obj.nextGreaterElements(nums))

