# coding:utf8

from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.helper(1, n, k, [], res)
        return res


    def helper(self, start, n, k, tmp, res):

        if len(tmp) == k:
            res.append(tmp[:])
            return

        for i in range(start, n + 1):
            self.helper(i + 1, n, k, tmp + [i], res)
	

if __name__ == '__main__':
    obj = Solution()
    n, k = 4, 2
    res = obj.combine(n, k)
    print(res)
