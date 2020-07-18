# encoding=utf8
"""
97. 交错字符串
给定三个字符串 s1, s2, s3, 验证 s3 是否是由 s1 和 s2 交错组成的。

示例 1:

输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
输出: true
示例 2:

输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
输出: false
"""
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        len_s1, len_s2, len_s3 = len(s1), len(s2), len(s3)
        if len_s1 + len_s2 != len_s3:
            return False
        dp = [[False] * (len_s2 + 1) for _ in range(len_s1 + 1)]

        dp[0][0] = True
        for i in range(1, len_s1 + 1):
            if s1[i-1] == s3[i-1]:
                dp[i][0] = True
            else:
                break

        for j in range(1, len_s2 + 1):
            if s2[j-1] == s3[j-1]:
                dp[0][j] = True
            else:
                break

        for i in range(1, len_s1 + 1):
            for j in range(1, len_s2 + 1):
                dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or (dp[i][j-1] and s2[j-1] == s3[i+j-1])

        return dp[len_s1][len_s2]


if __name__ == '__main__':
    s = Solution()
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    print s.isInterleave(s1, s2, s3)


