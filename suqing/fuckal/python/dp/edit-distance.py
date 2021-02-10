# coding:utf8
"""
    给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。
    你可以对一个单词进行如下三种操作：
    插入一个字符
    删除一个字符
    替换一个字符
    示例 1：
    输入：word1 = "horse", word2 = "ros"
    输出：3
    解释：
    horse -> rorse (将 'h' 替换为 'r')
    rorse -> rose (删除 'r')
    rose -> ros (删除 'e')

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/edit-distance
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
链接：https://leetcode-cn.com/problems/edit-distance
"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #return self.minDistance_v1(word1, word2)
        return self.minDistance_v2(word1, word2)
    def minDistance_v1(self, word1: str, word2: str) -> int:
        """
            记忆化递归
            分别从word1, word2的尾部开始
            if s1[i] == s2[j], i - 1, j - 1
            if s1[i] != s2[j], 三种情况, 增加, 删除, 修改, 取三种操作最终得到最小操作数
        """
        i, j = len(word1) - 1, len(word2) - 1
        memo = {}
        def dp(i, j) -> int:
            if (i, j) in memo:
                return memo[(i, j)]
            if i == -1:
                return j + 1
            if j == -1:
                return i + 1
            
            if word1[i] == word2[j]:
                memo[(i, j)] = dp(i - 1, j - 1)
            else:
                memo[(i, j)] = min(
                        dp(i - 1, j) + 1, # delete
                        dp(i, j - 1) + 1, # insert
                        dp(i - 1, j - 1) + 1 # update
                        )
                
            return memo[(i, j)]
        return dp(i, j)


            
    def minDistance_v2(self, word1: str, word2: str) -> int:
        """
            dp table
            定义: dp[i][j]表示word1[0..i] 和word2[0..j]的最小编辑距离
            if word1[i] == word2[j]
                dp[i][j] = dp[i - 1][j - 1]
            else
                dp[i][j] = min(dp[i - 1][j] + 1, dp[i - 1][j - 1] + 1, dp[i][j - 1] + 1)
        """
        if word1 == word2:
            return 0
        s1, s2 = len(word1), len(word2)
        dp = [[0] * (s2 + 1) for _ in range(s1 + 1)]
        # init
        for i in range(s1 + 1):
            dp[i][0] = i
        for j in range(s2 + 1):
            dp[0][j] = j

        for i in range(1, s1 + 1):
            for j in range(1, s2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(
                            dp[i - 1][j] + 1,
                            dp[i][j - 1] + 1,
                            dp[i - 1][j - 1] + 1)

        return dp[s1][s2]
    
    def minDistance_v2(self, word1: str, word2: str) -> int:
        """
            优化的dptable
        """

if __name__ == '__main__':
    word1, word2 = 'horse', 'ros'
    #word1, word2 = 'intention', 'execution'
    obj = Solution()
    print(obj.minDistance(word1, word2))
