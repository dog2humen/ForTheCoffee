# coding:utf8
from typing import List
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        return self.PredictTheWinner_v1(nums)	

    def PredictTheWinner_v1(self, nums: List[int]) -> bool:
        """ 
            recursive 
            计算当前做选择的玩家能赢过对手的分数, 如果大于0, 则能赢
            当前选择的分数 - 接下来对手赢过自己的分数
            eg. [1, 5, 2]
        """
        res = self.helper(nums, 0, len(nums) -1)
        return res >= 0
    
    def helper(self, nums, start, end):

        if start == end:
            return nums[start]

        nextLeft = nums[start] - self.helper(nums, start + 1, end)
        nextRight = nums[end] - self.helper(nums, start, end - 1)
        return max(nextLeft, nextRight)


if __name__ == '__main__':
    obj = Solution()
    nums = [1, 5, 2]
    res = obj.PredictTheWinner(nums)
    print(res)
