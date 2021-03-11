# coding:utf8
"""
    410. 分割数组的最大值
    给定一个非负整数数组 nums 和一个整数 m ，你需要将这个数组分成 m 个非空的连续子数组。
    设计一个算法使得这 m 个子数组各自和的最大值最小。
    输入：nums = [7,2,5,10,8], m = 2
    输出：18
    解释：
    一共有四种方法将 nums 分割为 2 个子数组。 其中最好的方式是将其分为 [7,2,5] 和 [10,8] 。
    因为此时这两个子数组各自的和的最大值为18，在所有情况中最小。
    链接：https://leetcode-cn.com/problems/split-array-largest-sum
"""
from typing import List
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        return self.splitArray_v1(nums, m)

    def splitArray_v1(self, nums: List[int], m: int) -> int:
        """
            二分查找思路
            定义连续子数组的最大和为max_sum, 它的取值范围为[max(nums), sum(nums)]
            最左二分max_sum的范围, 找到满足max_sum时, 能分割的连续子数组个数n == m
        """

        lo = max(nums)
        hi = sum(nums) + 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            n = self.split_arr(nums, mid)
            if n == m:
                hi = mid
            elif n < m:
                hi = mid # 最大子数组和太大了, 
            else:
                lo = mid + 1

        return lo

    
    def split_arr(self, nums: List[int], max_val: int) -> int:
        """
            当最大和为max_val时, 返回能分割的最小数组个数
        """
        sum_val = 0
        res = 1

        for i in range(len(nums)):
            if sum_val + nums[i] > max_val:
                res += 1
                sum_val = nums[i]
            else:
                sum_val += nums[i]

        return res

if __name__ == '__main__':
    nums = [7, 2, 5, 10, 8]
    m = 2
    obj = Solution()
    print(obj.splitArray(nums, m))

