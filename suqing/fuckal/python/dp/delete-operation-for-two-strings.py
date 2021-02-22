# coding:utf8
"""
     两个字符串的删除操作
     给定两个单词 word1 和 word2，找到使得 word1 和 word2 相同所需的最小步数，每步可以删除任意一个字符串中的一个字符。
     示例：
     输入: "sea", "eat"
     输出: 2
     解释: 第一步将"sea"变为"ea"，第二步将"eat"变为"ea"
     链接：https://leetcode-cn.com/problems/delete-operation-for-two-strings
"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        return self.minDistance_v1(word1, word2)
    def minDistance_v1(self, word1: str, word2: str) -> int:
        """
            删除的次数通过word1和word2的最长公共子序列的值推到
            res = len(word1) - lcs + len(word2) - lcs
        """
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return m - dp[m][n] + n - dp[m][n]
if __name__ == '__main__':
    word1 = 'sea'
    word2 = 'eat'
    obj = Solution()
    print(obj.minDistance(word1, word2))
