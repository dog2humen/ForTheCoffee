# coding:utf8
# 46 https://leetcode-cn.com/problems/permutations/

from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.helper(len(nums), nums, [], res)
        return res
    
    def helper(self, size, nums, curNums, res):
        if len(curNums) == size:
            res.append(curNums[:])
            return 
        for i, num in enumerate(nums):
            self.helper(size, nums[:i] + nums[i+1:], curNums + [num], res)


