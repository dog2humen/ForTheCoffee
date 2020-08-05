# coding:utf8
from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        #return self.rob_v1(nums)
        return self.rob_v2(nums)
    def rob_v1(self, nums: List[int]) -> int:
        """ 
            选择: 偷/不偷
            dp[i][j] 表示偷第i个房子的最高金额 ,j => 0 不偷, j => 1 偷
            状态转移方程:
                dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
                dp[i][1] = max(dp[i - 1][0] + nums[i], 0)

            初始化:
                dp[0][0] = 0
                dp[0][1] = nums[i]
        """
        if not nums:
            return 0
        dp = [[0] * 2 for _ in range(len(nums))]
        dp[0][0], dp[0][1] = 0, nums[0]

        for i in range(1, len(nums)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
            dp[i][1] = max(dp[i - 1][0] + nums[i], 0)

        return max(dp[-1][1], dp[-1][0])

    def rob_v2(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp_i_0, dp_i_1 = 0, nums[0] 

        for i in range(1, len(nums)):
            tmp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1)
            dp_i_1 = max(tmp + nums[i], 0)

        return max(dp_i_0, dp_i_1)



if __name__ == '__main__':
    obj = Solution()
    nums = [1,2,3,1]
    res = obj.rob(nums)
    print(res)
