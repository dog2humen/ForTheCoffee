# coding:utf8
from typing import List

class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        return self.findLength_v1(A, B)

    def findLength_v1(self, A: List[int], B: List[int]) -> int:
        '''
            dp[i][j] 表示A数组[...i]前i个, B数组[...j]前j个的最长公共子数组长度
            状态转移方程:
            if A[i] == A[j]: 表示当前元素可以加入到公共子串中
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = 0

        '''

        dp = [[0 for _ in range(len(B) + 1)] for _ in range(len(A) + 1)]
        res = 0
        for i in range(1, len(A) + 1):
            for j in range(1, len(B) + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                res = max(res, dp[i][j])
        return res


    
if __name__ == '__main__':
    A = [1,2,3,2,1]
    B = [3,2,1,4,7]
    obj = Solution()
    res = obj.findLength(A, B)
    print(res)
