# coding:utf8
from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        """
            dp[i][j] 偷第i个的最高金额, j => 0 不偷, j => 1 偷
            状态转移方程:
                size = len(nums)
                dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
                dp[i][1] = max(dp[i - 1][0] + nums[i], 0)

            初始化:
                dp[0][0] = 0, dp[0][1] = nums[0]

            环形收尾相接的话, 考虑两种情况分别求:
            1. 第1个偷, 最后一个不偷, 即求[0, size - 2] 
            2. 第1个不偷, 最后一个偷, 即求[1, size - 1]

        """

        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        return max(self.robRange(nums, 0, len(nums) - 2), self.robRange(nums, 1, len(nums) - 1))
    
    def robRange(self, nums, start, end):

        dp_i_0, dp_i_1 = 0, nums[start]
        for i in range(start + 1, end + 1):
            tmp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1)
            dp_i_1 = max(tmp + nums[i], 0)

        return max(dp_i_0, dp_i_1)



if __name__ == '__main__':
    obj = Solution()
    nums = [2,3,2]
    res = obj.rob(nums)
    print(res)

