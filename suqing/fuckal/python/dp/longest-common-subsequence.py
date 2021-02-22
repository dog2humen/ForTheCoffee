# coding:utf8
"""
     最长公共子序列
     给定两个字符串 text1 和 text2，返回这两个字符串的最长公共子序列的长度。
     一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
     例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。两个字符串的「公共子序列」是这两个字符串所共同拥有的子序列。
     若这两个字符串没有公共子序列，则返回 0。
     链接：https://leetcode-cn.com/problems/longest-common-subsequence
"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #return self.longestCommonSubsequence_v1(text1, text2)
        return self.longestCommonSubsequence_v2(text1, text2)

    def longestCommonSubsequence_v1(self, text1: str, text2: str) -> int:
        memo = [ [-1] * len(text2)  for _ in range(len(text1))]
        def dp(s1: str, i: int, s2: str, j: int) -> int:
            """
                表示s1[...i]与s2[...j]的最长公共子序列的长度
            """
            if i == len(s1) or j == len(s2):
                return 0
            if memo[i][j] != -1:
                return memo[i][j]
            if s1[i] == s2[j]:
                memo[i][j] = 1 + dp(s1, i + 1, s2, j + 1)
            else:
                # s1[i]不在lcs, s2[j]在
                # s2[i]在, s2[j]不在
                memo[i][j] = max(dp(s1, i + 1, s2, j),
                           dp(s1, i, s2, j + 1))
            return memo[i][j]

        return dp(text1, 0, text2, 0)

    def longestCommonSubsequence_v2(self, text1: str, text2: str) -> int:
        """
            dp table
            定义：s1[0..i-1] 和 s2[0..j-1] 的 lcs 长度为 dp[i][j]
            base case: dp[0][..] = dp[..][0] = 0
        """
        size1, size2 = len(text1), len(text2)
        dp = [[0] * (size2 + 1) for _ in range(size1 + 1)]
        
        for i in range(1, size1 + 1):
            for j in range(1, size2 + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        return dp[size1][size2]

if __name__ == '__main__':
    text1 = 'abcde'
    text2 = 'ace'
    obj = Solution()
    print(obj.longestCommonSubsequence(text1, text2))
