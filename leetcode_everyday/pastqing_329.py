# coding:utf8
from typing import List
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        return self.longestIncreasingPath_v1(matrix)

    def longestIncreasingPath_v1(self, matrix: List[List[int]]) -> int:
        '''
            递归回溯
        '''
        if not matrix:
            return 0
        rows, cols = len(matrix), len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                self.helper(matrix, i, j)

    def helper(self, matrix, rowIdx, colIdx):
        '''
            利用路径值来避免重复走
        '''
        res = 1
        # terminated
        if rowIdx < 0 or colIdx < 0 or rowIdx >= len(matrix) or colIdx >= len(matrix[0]):
            return


        # current level
        # drill down
        if matrix[rowIdx][colIdx] < matrix[rowIdx - 1][colIdx]:
            res = max(res, self.helper(matrix, rowIdx - 1, colIdx) + 1) # 上
        if matrix[rowIdx][colIdx] < matrix[rowIdx + 1][colIdx]:
            res = max(res, self.helper(matrix, rowIdx + 1, colIdx) + 1) # 下
        if matrix[rowIdx][colIdx] < matrix[rowIdx][colIdx - 1]:
            res = max(res, self.helper(matrix, rowIdx, colIdx - 1) + 1) # 左
        if matrix[rowIdx][colIdx] < matrix[rowIdx][colIdx + 1]:
            res = max(res, self.helper(matrix, rowIdx, colIdx + 1) + 1)# 右
        
        return res




if __name__ == '__main__':
    obj = Solution()
    matrix = [[9,9,4],[6,6,8],[2,1,1]]
    obj.longestIncreasingPath(matrix)
