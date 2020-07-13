# encoding=utf8
"""
718. 最长重复子数组
给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。

输入：
A: [1,2,3,2,1]
B: [3,2,1,4,7]
输出：3
解释：
长度最长的公共子数组是 [3, 2, 1] 。
"""
import numpy as np
class Solution(object):
    # 超时
    def findLength_pass(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        if not A or not B:
            return 0
        row = len(A)
        col = len(B)
        matrix = np.zeros(row*col, np.int).reshape(col, row)
        for i in range(row):
            for j in range(col):
                if A[i] == B[j]:
                    matrix[i][j] = 1
        print matrix

        res_max = 0
        for i in range(row):
            for j in range(col):
                a, b = i, j
                cur = 0
                while a < row and b < col and matrix[a][b] == 1:
                    cur += 1
                    res_max = max(res_max, cur)
                    a += 1
                    b += 1
        return res_max

    #  滑动窗口解法
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        if not A or not B:
            return 0

        len_a = len(A)
        len_b = len(B)

        res_max = 0
        for i in range(len_a):
            length = min(len_b, len_a - i)
            res_max = max(res_max, self.max_length(A, B, i, 0, length))

        for i in range(len_b):
            length = min(len_a, len_b - i)
            res_max = max(res_max, self.max_length(A, B, 0, i, length))
        return res_max

    def max_length(self, A, B, start_a, start_b, length):
        res = cur = 0
        for i in range(length):
            if A[start_a + i] == B[start_b + i]:
                cur += 1
                res = max(cur, res)
            else:
                cur = 0
        return res

    # dp 解法 
    def findLength_dp(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        if not A or not B:
            return 0

        len_a = len(A)
        len_b = len(B)
        matrix = [[0 for i in range(len_a + 1)] for i in range(len_b + 1)]

        res_max = 0
        for i in range(len_a+1)[1:]:
            for j in range(len_b+1)[1:]:
                if A[i-1] == B[j-1]:
                    matrix[i][j] = matrix[i-1][j-1] + 1
                res_max = max(matrix[i][j], res_max)

        return res_max

s = Solution()
print s.findLength_dp([1,2,3,2,1],[3,2,1,4,7])
