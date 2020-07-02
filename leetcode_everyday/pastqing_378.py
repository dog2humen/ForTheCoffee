# coding:utf8

from typing import List
import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        #return self.kthSmallest_v1(matrix, k)
        return self.kthSmallest_v2(matrix, k)
    def kthSmallest_v1(self, matrix: List[List[int]], k: int) -> int:
        '''
            遍历数组, 构建堆, 利用堆找第k小
            python 库heapq 是小顶堆
        '''
        matrix_data = list(self.flatten(matrix))
        heapq.heapify(matrix_data)

        for _ in range(k - 1):
            heapq.heappop(matrix_data)

        return heapq.heappop(matrix_data) 




    def flatten(self, iterable):
        from collections.abc import Iterable
        for item in iterable:
            if isinstance(item, Iterable):
                yield from self.flatten(item)
            else:
                yield item


    def kthSmallest_v2(self, matrix: List[List[int]], k: int) -> int:
        '''
            二分查找:
            思路: 
            1. 对值域进行二分, 范围是[matrix[0][0], matrix[-1][-1]], 即左上角和右下角
            2. 第k小值就在这个范围内
            3. 取范围的mid值, 找出矩阵中<=mid值的个数c, 如果c < k 则意味着mid值小了, 如果 c > k 则意味着mid值大了
            4. 如何统计不大于mid值的元素个数:
                与每行最右边数比, 如果比它大则往走到下一行


        '''
        low, high = matrix[0][0], matrix[-1][-1]
        while low <= high:
            mid = low + (high - low) // 2
            c = self.getMatrixCount(matrix, mid)
            if c < k:
                low = mid + 1
            else:
                high = mid - 1

        return low
    
    def getMatrixCount(self, matrix, val):
        c = 0
        row, col = 0, len(matrix[0]) - 1
        while row < len(matrix) and col >= 0:
            if val >= matrix[row][col]:
                c += col + 1
                row += 1
            else:
                col -= 1

        return c


if __name__ == '__main__':
    input = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
    obj = Solution()
    res = obj.kthSmallest_v2(input, 8)
    print(res)

            
