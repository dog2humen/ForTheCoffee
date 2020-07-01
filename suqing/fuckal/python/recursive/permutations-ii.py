# coding:utf8
# 47 https://leetcode-cn.com/problems/permutations-ii/

from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        '''
            [1, 1, 2]
        '''
        res = []
        nums.sort()
        self.helper(len(nums), nums, [], res)
        return res
    def helper(self, size, nums, curNums, res):
        if len(curNums) == size:
            print(curNums)
            res.append(curNums[:])
            return
        
        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            self.helper(size, nums[:i] + nums[i+1:], curNums + [num], res)


if __name__ == '__main__':
    input = [1, 1, 2]
    obj = Solution()
    obj.permuteUnique(input)
