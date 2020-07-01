# coding:utf8
# 51 https://leetcode-cn.com/problems/n-queens/
from typing import List
class Solution:
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        '''
            一层一层遍历, 选择合适的位置
        '''

        
    def helper(self, n, curPath, res):
        if n == len(curPath):
            res.append(curPath[:])
            return

        for i in range(n):


