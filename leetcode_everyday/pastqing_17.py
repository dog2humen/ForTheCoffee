# coding:utf8
from typing import List
class Solution:
    def letterCombinations(self, digs) -> List[str]:
        return self.letterCombinations_v1(digs)
    def letterCombinations_v1(self, digs) -> List[str]:
        if not digs:
            return []

        dmaps = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
        } 

        size = len(digs)
        chs = [list(dmaps.get(dig)) for dig in digs]
        res = []
        self.helper(0, chs, [], size, res)
        return res
    def helper(self, idx, chs, cur, size, res):

        if len(cur) == size or idx >= size:
            res.append(''.join(cur))
            return

        for ch in chs[idx]:
            self.helper(idx + 1, chs, cur + [ch], size, res)


if __name__ == '__main__':
    obj = Solution()
    digs = '23'
    res = obj.letterCombinations(digs)
    print(res)

