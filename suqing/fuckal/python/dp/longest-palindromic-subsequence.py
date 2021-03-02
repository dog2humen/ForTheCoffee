# coding:utf8
"""
    最长回文子序列
    给定一个字符串 s ，找到其中最长的回文子序列，并返回该序列的长度。
    可以假设 s 的最大长度为 1000 。
    示例 1:
    输入:
    "bbbab"
    输出:
    4
    链接：https://leetcode-cn.com/problems/longest-palindromic-subsequence
"""
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        return self.longestPalindromeSubseq_v1(s)

    def longestPalindromeSubseq_v1(self, s: str) -> int:
        """
            dp table
            定义: dp[i][j]表示s[i...j]的最长回文子序列
            dp[i][j] 的结果可以由dp[i + 1][j - 1]转移而来
            if s[i] == s[j] dp[i][j] = 2 + dp[i + 1][j - 1]
            if s[i] != s[j] dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])
            base case:
                i == j dp[i][j] = 1
                i > j dp[i][j] = 0
        """

        size = len(s)
        dp = [[0] * size for _ in range(size)]
        for i in range(size):
            dp[i][i] = 1

        # 反着遍历, 以为dp[i][j]可以由三个方向转移而来: 左, 左下, 下

        for i in range(size - 1, -1, -1):
            for j in range(i + 1, size):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])

        return dp[0][size - 1]

if __name__ == '__main__':
    s = 'bbbab'
    obj = Solution()
    print(obj.longestPalindromeSubseq(s))

