# coding:utf8
"""
    220. 存在重复元素 III
    给你一个整数数组 nums 和两个整数 k 和 t 。请你判断是否存在 两个不同下标 i 和 j，使得 abs(nums[i] - nums[j]) <= t ，同时又满足 abs(i - j) <= k 。

    如果存在则返回 true，不存在返回 false。

    示例 1：
    输入：nums = [1,2,3,1], k = 3, t = 0
    输出：true

    链接：https://leetcode-cn.com/problems/contains-duplicate-iii
"""

from typing import List

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        return self.containsNearbyAlmostDuplicate_v1(nums, k, t)

    def containsNearbyAlmostDuplicate_v1(self, nums: List[int], k: int, t: int) -> bool:
        left, right = 0, 0
        size = len(nums)
        while right < size:
            num = nums[right]
            
            while 0 < right - left <= k:
                print(left, right, nums[left], nums[right])
                if abs(nums[left] - nums[right]) <= t:
                    return True
                left += 1

            right += 1

        return False


if __name__ == '__main__':
    nums, k, t = [1, 2, 3, 1], 3, 0
    obj = Solution()
    print(obj.containsNearbyAlmostDuplicate(nums, k, t))

