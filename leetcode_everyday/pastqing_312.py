# coding:utf8
from typing import List
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        return self.maxCoins_v1(nums)
    def maxCoins_v1(self, nums: List[int]) -> int:
        '''
            回溯
        '''
        # 边界添加1
        newNums = [1]
        newNums.extend(nums)
        newNums.append(1)

        memo = {}
        return self.helper(newNums, memo, 0, len(newNums) - 1)
    def helper(self, nums, memo, left, right):
        # terminated
        if left + 1 == right:
            return 0
        if (left, right) in memo:
            return memo[(left, right)]

        # current level
        res = 0
        for i in range(left + 1, right):
            res = max(res, nums[left] * nums[i] * nums[right] 
            + self.helper(nums, memo, left, i)
            + self.helper(nums, memo, i, right))
        memo[(left, right)] = res

        return res

if __name__ == '__main__':
    obj = Solution()
    nums = [3,1,5,8]
    res = obj.maxCoins(nums)
    print(res)

