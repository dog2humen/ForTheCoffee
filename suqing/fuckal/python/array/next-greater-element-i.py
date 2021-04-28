# coding:utf8
"""
    496. 下一个更大元素 I
    给你两个 没有重复元素 的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。
    请你找出 nums1 中每个元素在 nums2 中的下一个比其大的值。
    nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。如果不存在，对应位置输出 -1 。

输入: nums1 = [4,1,2], nums2 = [1,3,4,2].
输出: [-1,3,-1]
解释:
    对于 num1 中的数字 4 ，你无法在第二个数组中找到下一个更大的数字，因此输出 -1 。
    对于 num1 中的数字 1 ，第二个数组中数字1右边的下一个较大数字是 3 。
    对于 num1 中的数字 2 ，第二个数组中没有下一个更大的数字，因此输出 -1 。

    链接：https://leetcode-cn.com/problems/next-greater-element-i
"""
from typing import List
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return self.nextGreaterElement_v1(nums1, nums2)

    def nextGreaterElement_v1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
            单调栈思路, 
            利用单调栈将nums2中的每个元素比他单调的元素记录下来
        """
        res = {}
        stack = []
        for i in range(len(nums2) - 1, -1, -1):

            while stack and stack[-1] <= nums2[i]:
                stack.pop()

            # nums2[i] 的next greate number 
            res[nums2[i]] = stack[-1] if stack else -1
            stack.append(nums2[i])


        return [res[i] for i in nums1]


if __name__ == '__main__':
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]
    obj = Solution()
    print(obj.nextGreaterElement(nums1, nums2))
