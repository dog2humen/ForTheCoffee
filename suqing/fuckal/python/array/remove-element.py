# coding:utf8
"""
    27. 移除元素
    给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。

    不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。

    元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

输入：nums = [3,2,2,3], val = 3
输出：2, nums = [2,2]
解释：函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。你不需要考虑数组中超出新长度后面的元素。例如，函数返回的新长度为 2 ，而 nums = [2,2,3,3] 或 nums = [2,2,0,0]，也会被视作正确答案。

    链接：https://leetcode-cn.com/problems/remove-element
"""

from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        return self.removeElement_v1(nums, val)
        #return self.removeElement_v2(nums, val)
    def removeElement_v1(self, nums: List[int], val: int) -> int:

        size = len(nums)
        if size == 0:
            return 0

        p1, p2 = 0, size

        while p1 < p2:
            if nums[p1] == val:
                nums[p1] = nums[p2 - 1]
                p2 -= 1
            else:
                p1 += 1

        return p2

    def removeElement_v2(self, nums: List[int], val: int) -> int:

        p = 0
        for num in nums:
            if num != val:
                nums[p] = num
                p += 1
        return p


if __name__ == '__main__':
    nums, val = [3, 2, 2, 3], 3
    nums, val = [0,1,2,2,3,0,4,2], 2
    obj = Solution()
    print(obj.removeElement(nums, val))
