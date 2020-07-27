# coding:utf8
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        return self.isSubsequence_v1(s, t)
    def isSubsequence_v1(self, s: str, t: str) -> bool:
        '''
            s = "abc", t = "ahbgdc" true
            s = "axc", t = "ahbgdc" false
        '''
        slen, tlen = len(s), len(t)
        i, j = 0, 0
        while i < slen and j < tlen:
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == slen

    def isSubsequence_v2(self, s: str, t: str) -> bool:
        pass

if __name__ == '__main__':
    obj = Solution()
    s = 'axc'
    t = 'ahbgdc'
    res = obj.isSubsequence(s, t)
    print(res)
