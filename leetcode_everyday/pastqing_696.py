# coding:utf8
from collections import Counter

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        #return self.countBinarySubstrings_v1(s)
        return self.countBinarySubstrings_v2(s)
    def countBinarySubstrings_v1(self, s: str) -> int:
        """
            eg. "00110011" => 6,  0011，01，1100，10，0011 和 01
            0001111 min(3, 4) => 3, {01, 0011, 000111}
        """

        if not s:
            return 0

        res, cur, pre = 0, 1, 0
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                cur += 1
            else:
                res += min(cur, pre)
                pre = cur
                cur = 1

        return res + min(cur, pre)

    def countBinarySubstrings_v2(self, s: str) -> int:
        if not s:
            return 0

        s = map(len, s.replace('01', '0 1').replace('10', '1 0').split())
        s = list(s)
        """[1, 2, 3, 4], [2, 3, 4]"""
        return sum(min(a, b) for a, b in zip(s, s[1:]))



if __name__ == '__main__':
    obj = Solution()
    s = '00110011'
    res = obj.countBinarySubstrings(s)
    print(res)
    


