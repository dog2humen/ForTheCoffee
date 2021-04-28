# coding:utf8
"""
    438. 找到字符串中所有字母异位词
    给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。
    字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。
    说明：
    字母异位词指字母相同，但排列不同的字符串。
    不考虑答案输出的顺序。
    输入:
    s: "cbaebabacd" p: "abc"

    输出:
    [0, 6]
    解释:
    起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。
    起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词。

    链接：https://leetcode-cn.com/problems/find-all-anagrams-in-a-string
"""
from typing import List
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        return self.findAnagrams_v1(s, p)

    def findAnagrams_v1(self, s: str, p: str) -> List[int]:
        """
            滑动窗口
        """
        from collections import Counter
        from collections import defaultdict

        needs = Counter(p) 
        window = defaultdict(int)
        left, right, valid = 0, 0, 0
        res = []
        while right < len(s):
            c = s[right]
            right += 1
            if c in needs:
                window[c] += 1
                if window[c] == needs[c]:
                    valid += 1


            while right - left >= len(p):
                if valid == len(needs):
                    res.append(left)
                d = s[left]
                left += 1
                if d in needs:
                    if window[d] == needs[d]:
                        valid -= 1
                    window[d] -= 1
        return res




if __name__ == '__main__':
    s = 'cbaebabacd'
    p = 'abc'
    obj = Solution()
    print(obj.findAnagrams(s, p))
