# coding:utf-8
# 78 https://leetcode-cn.com/problems/subsets/
from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.helper(nums, [], res)
        return res

    def helper(self, nums, curNums, res):
        res.append(curNums)
        for i, num in enumerate(nums):
            self.helper(nums[i + 1:], curNums + [num], res)


