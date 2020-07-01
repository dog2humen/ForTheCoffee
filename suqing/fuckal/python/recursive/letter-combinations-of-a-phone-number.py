# coding:utf-8
# 17 https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/
from typing import List

class Solution:

    def letterCombinations(self, digs) -> List[str]:
        """
            input: "23"
            output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
        """

        maps = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
        }

        letters = [list(maps.get(n)) for n in digs if n in maps]
        if not letters:
            return []
        res = []
        self.helper(0, len(digs), letters, [], res)
        return res
    
    def helper(self, level, size, letters, curs, res):

        if len(curs) == size:
            res.append(''.join(curs))
            return 

        for ch in letters[level]:
            self.helper(level + 1, size, letters, curs + [ch], res)

if __name__ == '__main__':
    obj = Solution()
    input = ''
    res = obj.letterCombinations(input)
    print(res)
