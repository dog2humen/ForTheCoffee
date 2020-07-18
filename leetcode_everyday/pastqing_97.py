# coding:utf8

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        return self.isInterleave_v1(s1, s2, s3)
    def isInterleave_v1(self, s1: str, s2: str, s3: str) -> bool:
        '''
            按照不同路径的思路dp, 从s1, s2构建的二维矩阵中找到一条等于s3的
            定义: dp[i][j] 为s1, 以i为结尾的, s2以j为结尾能否构建s3的(True/False)
            状态转移方程:
                i = 0, j = 0 分别表示空串
                dp[i][j] = (dp[i - 1][j] and s3[i + j - 1] == s1[i - 1]) || (dp[i][j - 1] and s3[i + j - 1] == s2[j - 1])
        '''
        
        size_1, size_2 = len(s1), len(s2)
        if (size_1 + size_2) != len(s3):
            return False
        dp = [[False] * (size_2 + 1) for _ in range(size_1 + 1)]
        dp[0][0] = True
        for i in range(1, size_1 + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]

        for i in range(1, size_2 + 1):
            dp[0][i] = dp[0][i - 1] and s2[i - 1] == s3[i - 1]

        
        for i in range(1, size_1 + 1):
            for j in range(1, size_2 + 1):
                dp[i][j] = (dp[i - 1][j] and s3[i + j - 1] == s1[i - 1]) or (dp[i][j - 1] and s3[i + j - 1] == s2[j - 1])


        return dp[-1][-1]


if __name__ == '__main__':
    obj = Solution()
    s1 = ''
    s2 = ''
    s3 = 'a'
    res = obj.isInterleave(s1, s2, s3)
    print(res)

