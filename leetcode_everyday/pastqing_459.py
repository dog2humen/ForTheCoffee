# coding:utf8
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return self.repeatedSubstringPattern_v1(s)
    def repeatedSubstringPattern_v1(self, s: str) -> bool:
        """
            abcabcabcabc
            如果存在重复的字符串构成整个字符串, 那么这个重复的子串长度不会大于len(s)
            1. 第一个字符是重复子串的第一个字符
            2. 最后一个字符串是重复字串的最后一个字符
            3. S1 = 2 * s
            4. s2 = s1[1:-1] 去掉头尾字符 bc abcabcabcabcabcabc ab
            5. 如果有重复, 则s in s2

        """

        return s in (s * 2)[1 : -1]

if __name__ == '__main__':
    obj = Solution()
    s = 'abcabcabcabc'
    res = obj.repeatedSubstringPattern(s)
    print(res)
