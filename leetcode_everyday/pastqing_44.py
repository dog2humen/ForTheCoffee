# coding:utf8
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return self.isMatch_v1(s, p)

    def isMatch_v1(self, s, p):
        '''
            dp解法
            dp[i][j]表示字符串s前i个与模式串p前j个能否匹配(True or False)
            状态转移方程:
                if p[j] in [a - z] AND s[i] == p[j]: 匹配上了
                    dp[i][j] = dp[i - 1][j - 1]
                if p[j] == '?':
                    dp[i][j] = dp[i - 1][j - 1]
                if p[j] == '*': # * 可以匹配0个或多个
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]

            初始状态:
                dp[0][0] = True 表示模式串p为空, s为空
                dp[i][0] = False
                p第一个是*,*可以匹配空串, 则dp[0][1] = True

        '''
        
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[0][0] = True
        for j in range(1, len(p) + 1):
            if p[j - 1] == '*':
                dp[0][j] = True
            else:
                break
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
                elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
        
        return dp[-1][-1]


if __name__ == '__main__':
    s = ''
    p = '*'
    #s = 'adceb'
    #p = '*a*b'
    obj = Solution()
    res = obj.isMatch(s, p)
    print(res)

