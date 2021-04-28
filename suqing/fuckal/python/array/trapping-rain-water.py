# coding:utf8
"""
    给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
    输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
    输出：6
    解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 

    链接：https://leetcode-cn.com/problems/trapping-rain-water
"""

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        #return self.trap_v1(height)
        return self.trap_v2(height)
    def trap_v1(self, height: List[int]) -> int:
        """
            暴力
            某个位置i的雨水量为, min(max(height[0...i), max(height[i + 1...]))
        """
        size = len(height)
        res = 0
        for i in range(1, size - 1):
            left_max, right_max = 0, 0
            for j in range(i + 1):
                left_max = max(left_max, height[j])

            for j in range(i, size):
                right_max = max(right_max, height[j])

            res = res + min(left_max, right_max) - height[i]

        return res

    def trap_v2(self, height: List[int]) -> int:
        """
            双指针
        """
        res = 0
        size = len(height)
        left, right = 0, size - 1
        left_max, right_max = height[left], height[right]

        while left <= right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])

            if left_max < right_max:
                res += left_max - height[left]
                left += 1
            else:
                res += right_max - height[right]
                right -= 1

        return res

if __name__ == '__main__':
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    obj = Solution()
    print(obj.trap(height))




