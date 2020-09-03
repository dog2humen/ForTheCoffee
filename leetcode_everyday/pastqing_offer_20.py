# coding:utf8
"""
	请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。例如，字符串"+100"、"5e2"、"-123"、"3.1416"、"-1E-16"、"0123"都表示数值，但"12e"、"1a3.14"、"1.2.3"、"+-5"及"12e+5.4"都不是。
"""
class Solution:
    def isNumber(self, s: str) -> bool:
        return self.isNumber_v2(s)

    def isNumber_v1(self, s: str) -> bool:
        """
            dp思路:
            定义: dp[i]表示s[0..i]是否可以表示为数值
            状态转移方程:
            
        """
        pass

    def isNumber_v2(self, s: str) -> bool:
        """
            暴力
        """
        if not s:
            return False

        hasNum, hasE, hasDot = False, False, False

        s = s.strip()
        for i, val in enumerate(s):
            if '0' <= val <= '9':
                hasNum = True

            elif val == '.':
                # . 前不能有.或者e
                if hasDot or hasE:
                    return False
                hasDot = True
            elif val == 'e' or val == 'E':
                # e前不能有e或者没数字
                if hasE or not hasNum:
                    return False
                hasE = True
                hasNum = False # 0e
            elif val == '+' or val == '-':
                if i != 0 and s[i - 1] not in ('e', 'E'):
                    return False
            else:
                return False

            
        return hasNum



            
if __name__ == '__main__':
    obj = Solution()
    s = " 005047e+6"
    res = obj.isNumber(s)
    print(res)
