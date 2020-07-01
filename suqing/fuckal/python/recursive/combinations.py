# coding:utf8
# 77 https://leetcode-cn.com/problems/combinations/
from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.helper(1, n, k ,[], res)
        return res

    def helper(self, idx, n, k, curNums, res):
        if len(curNums) == k:
            res.append(curNums[:])
            return

        for i in range(idx, n + 1):
            self.helper(i + 1, n, k, curNums + [i], res)
