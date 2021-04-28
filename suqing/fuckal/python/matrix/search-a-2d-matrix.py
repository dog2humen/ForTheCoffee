# coding:utf8
"""
    74. 搜索二维矩阵
    编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

    每行中的整数从左到右按升序排列。
    每行的第一个整数大于前一行的最后一个整数。
     
    链接：https://leetcode-cn.com/problems/search-a-2d-matrix
"""
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return self.searchMatrix_v1(matrix, target)
    def searchMatrix_v1(self, matrix: List[List[int]], target: int) -> bool:
        pass


if __name__ == '__main__':
    matrix = [
            [1, 3, 5, 7],
            [10, 11, 16, 20],
            [23, 30, 34, 60]
            ]
    target = 3
    obj = Solution()
    print(obj.searchMatrix(matrix, target))
