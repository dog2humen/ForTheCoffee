# coding:utf8

from typing import List
import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        return self.kthSmallest_v1(matrix, k)
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
        pass


if __name__ == '__main__':
    input = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
    obj = Solution()
    res = obj.kthSmallest_v1(input, 2)
    print(res)

            
