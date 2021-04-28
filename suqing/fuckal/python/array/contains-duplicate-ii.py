# coding:utf8
"""
    219. 存在重复元素 II
    给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的 绝对值 至多为 k。

    示例 1:
    输入: nums = [1,2,3,1], k = 3
    输出: true
    链接：https://leetcode-cn.com/problems/contains-duplicate-ii
"""
from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        return self.containsNearbyDuplicate_v1(nums, k)

    def containsNearbyDuplicate_v1(self, nums: List[int], k: int) -> bool:
        
        from collections import defaultdict
        size = len(nums)
        left, right = 0, 0
        #window = defaultdict(int)
        window = set()

        while right < size:
            num = nums[right]
            if num in window:
                return True
            window.add(num)
            if len(window) > k:
                window.remove(nums[right - k])

            right += 1

        return False


if __name__ == '__main__':
    nums, k = [1, 2, 3, 1], 3
    obj = Solution()
    print(obj.containsNearbyDuplicate(nums, k))

