# coding:utf8
"""
    862. 和至少为 K 的最短子数组
    返回 A 的最短的非空连续子数组的长度，该子数组的和至少为 K 。
    如果没有和至少为 K 的非空子数组，返回 -1 。
    输入：A = [1], K = 1
    输出：1
"""
from typing import List
class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        return self.shortestSubarray_v1(A, K)

    def shortestSubarray_v1(self, A: List[int], K: int) -> int:
        """
            前缀和+单调栈思路:
            使用单调递增栈来记录递增性的前缀和序列，随后在有序的单调栈序列中用二分搜索
        """

        stack = [(0, -1)] # 前缀和单调递增栈
        res = float('inf')
        cur_sum = 0 
        for i in range(len(A)):
            
            cur_sum += A[i] 
            print(stack)
            while stack and stack[-1][0] >= cur_sum:
                stack.pop()

            idx = self.binarySearch(stack, cur_sum - K)
            if idx > 0:
                res = min(res, i - stack[idx - 1][1])

            stack.append((cur_sum, i))

        return -1 if res == float('inf') else res


    def binarySearch(self, arr, target):

        lo, hi = 0, len(arr)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if arr[mid][0] > target:
                hi = mid
            else:
                lo = mid + 1
        return lo

if __name__ == '__main__':
    A, K = [2, -1, 2], 3
    obj = Solution()
    print(obj.shortestSubarray(A, K))
