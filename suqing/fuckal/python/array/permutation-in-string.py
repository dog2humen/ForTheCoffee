# coding:utf8
"""
    567. 字符串的排列
    给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。
    换句话说，第一个字符串的排列之一是第二个字符串的子串。
    输入: s1 = "ab" s2 = "eidbaooo"
    输出: True
    解释: s2 包含 s1 的排列之一 ("ba").
    https://leetcode-cn.com/problems/permutation-in-string/
"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        return self.checkInclusion_v1(s1, s2)

    def checkInclusion_v1(self, s1: str, s2: str) -> bool:
        from collections import Counter
        from collections import defaultdict

        needs = Counter(s1)
        window = defaultdict(int)
        left, right, valid = 0, 0, 0

        while right < len(s2):
            c = s2[right]
            right += 1
            if c in needs:
                window[c] += 1
                if window[c] == needs[c]:
                    valid += 1

            while right - left >= len(s1):
                if valid == len(needs):
                    return True
                d = s2[left]
                left += 1
                if d in needs:
                    if window[d] == needs[d]:
                        valid -= 1
                    window[d] -= 1


        return False




if __name__ == '__main__':
    s1, s2 = 'ab', 'eidbaooo'
    obj = Solution()
    print(obj.checkInclusion(s1, s2))
