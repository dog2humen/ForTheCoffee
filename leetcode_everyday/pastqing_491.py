# coding:utf8
from typing import List

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        return self.findSubsequences_v1(nums)
    def findSubsequences_v1(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.helper(nums, 0, [], res)
        return res
    
    def helper(self, nums, start, cur, res):
        
        if len(cur) > 1:
            res.append(cur[:])

        memo = set()
        for i in range(start, len(nums)):
            if nums[i] in memo:
                continue
            if len(cur) == 0 or cur[-1] <= nums[i]:
                memo.add(nums[i])
                self.helper(nums, i + 1, cur + [nums[i]], res)

if __name__ == '__main__':
    obj = Solution()
    nums = [4, 6, 7, 7]
    #nums = [4, 3, 2, 1]
    res = obj.findSubsequences(nums)
    print(res)
