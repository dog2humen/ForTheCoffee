# encoding=utf8
"""
17. 电话号码的字母组合
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

示例:
输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
说明:
尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。
"""
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        return self.letterCombinations_v1(digits)

    def letterCombinations_v1(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return list()
        res = list()
        tmp = list()
        phone_map = {'2':'abc',
                     '3':'def',
                     '4':'ghi',
                     '5':'jkl',
                     '6':'mno',
                     '7':'pqrs',
                     '8':'tuv',
                     '9':'wxyz'}

        def dfs(n):
            if n == len(digits):
                res.append(''.join(tmp))
                return
            #else:
            digit = digits[n]
            for letter in phone_map[digit]:
                tmp.append(letter)
                dfs(n + 1)
                tmp.pop()
        dfs(0)
        return res


if __name__ == '__main__':
    s = Solution()
    print s.letterCombinations('23')


