# coding:utf8
"""
    80. 删除有序数组中的重复项 II
    给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 最多出现两次 ，返回删除后数组的新长度。

    不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

输入：nums = [1,1,1,2,2,3]
输出：5, nums = [1,1,2,2,3]
解释：函数应返回新长度 length = 5, 并且原数组的前五个元素被修改为 1, 1, 2, 2, 3 。 不需要考虑数组中超出新长度后面的元素。

    链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array-ii
"""

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        from collections import defaultdict
        size = len(nums)
        if size == 0:
            return 0

        cache = defaultdict(int)
        p1, p2 = 0, 1
        while p2 < size:
            cache[nums[p1]] += 1
            if nums[p2] != nums[p1]:
                p1 += 1
                nums[p1] = nums[p2]

            else:
                if cache[nums[p1]] < 2:
                    p1 += 1
                    nums[p1] = nums[p2]
            p2 += 1
        return p1 + 1



if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    #nums = [0, 0, 1, 2, 2, 2, 3]
    obj = Solution()
    print(obj.removeDuplicates(nums))
