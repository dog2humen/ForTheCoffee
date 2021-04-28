# coding:utf8
"""
    209. 长度最小的子数组
    给定一个含有 n 个正整数的数组和一个正整数 target 。
    找出该数组中满足其和 ≥ target 的长度最小的连续子数组 
    [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。
    如果不存在符合条件的子数组，返回 0
输入：target = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。
    链接：https://leetcode-cn.com/problems/minimum-size-subarray-sum
"""
from typing import List 
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #return self.minSubArrayLen_v1(target, nums)
        return self.minSubArrayLen_v2(target, nums)
    def minSubArrayLen_v1(self, target: int, nums: List[int]) -> int:
        """
            前缀和+二分查找
            pre_sums 为nums的前缀和
            pre_sums[0] = 0, pre_sums[i] 表示nums[0...i - 1]的和

        """
        pre_sums = [0]
        res = len(nums) + 1
        # 构造前缀和
        for i in range(len(nums)):
            pre_sums.append(pre_sums[-1] + nums[i])

        for i in range(1, len(pre_sums)):
            # pre_sums[index] - pre_sums[i]
            t = pre_sums[i - 1] + target
            index = self.binary_search_left(pre_sums, t)

            if index != len(pre_sums):
                res = min(res, index - (i - 1))

        return 0 if res == len(pre_sums) else res

    def binary_search_left(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] >= target:
                hi = mid
            elif nums[mid] < target:
                lo = mid + 1

        return lo


    def minSubArrayLen_v2(self, target: int, nums: List[int]) -> int:
        """
            滑动窗口
        """
        left, right = 0, 0
        cur_sums = 0

        res = float('inf')

        while right < len(nums):
            n = nums[right]
            cur_sums += n
            right += 1

            while cur_sums >= target:
                res = min(res, right - left)
                cur_sums -= nums[left]
                left += 1
                

        return 0 if res == float('inf') else res 
        

if __name__ == '__main__':
    nums = [2, 3, 1, 2, 4, 3]
    target = 7
    obj = Solution()
    print(obj.minSubArrayLen(target, nums))

