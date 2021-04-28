# coding:utf8
"""
    两个字符串的最小ASCII删除和
    给定两个字符串s1, s2，找到使两个字符串相等所需删除字符的ASCII值的最小和。
    示例 1:
    输入: s1 = "sea", s2 = "eat"
    输出: 231
    解释: 在 "sea" 中删除 "s" 并将 "s" 的值(115)加入总和。
    在 "eat" 中删除 "t" 并将 116 加入总和。
    结束时，两个字符串相等，115 + 116 = 231 就是符合条件的最小和。
    链接：https://leetcode-cn.com/problems/minimum-ascii-delete-sum-for-two-strings
"""
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        return self.minimumDeleteSum_v1(s1, s2)

    def minimumDeleteSum_v1(self, s1: str, s2: str) -> int:
        memo = [[-1] * len(s2) for _ in range(len(s1))]
        def dp(s1: str, i: int, s2: str, j: int) -> int:
            res = 0
            if i == len(s1):
                for k in range(j, len(s2)):
                    res += ord(s2[k])
                return res

            if j == len(s2):
                for k in range(i, len(s1)):
                    res += ord(s1[k])
                return res

            if memo[i][j] != -1:
                return memo[i][j]

            if s1[i] == s2[j]: # 不用删
                memo[i][j] = dp(s1, i + 1, s2, j + 1)
            else: # 删其中一个
                memo[i][j] = min(ord(s1[i]) + dp(s1, i + 1, s2, j), 
                                 ord(s2[j]) + dp(s1, i, s2, j + 1))

            return memo[i][j]
        return dp(s1, 0, s2, 0)

if __name__ == '__main__':
    s1 = 'sea'
    s2 = 'eat'
    obj = Solution()
    print(obj.minimumDeleteSum(s1, s2))
