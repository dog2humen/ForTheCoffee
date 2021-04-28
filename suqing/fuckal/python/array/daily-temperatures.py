# coding:utf8
"""
    739. 每日温度
    请根据每日 气温 列表，重新生成一个列表。对应位置的输出为：要想观测到更高的气温，至少需要等待的天数。如果气温在这之后都不会升高，请在该位置用 0 来代替。

    例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。

    链接：https://leetcode-cn.com/problems/daily-temperatures
"""

from typing import List
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        return self.dailyTemperatures_v1(T)
    def dailyTemperatures_v1(self, T: List[int]) -> List[int]:
        """
            单调栈思路
        """
        stack = []
        res = []
        for i in range(len(T) - 1, -1, -1):
            
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()

            res.insert(0, stack[-1] - i if stack else 0)
            stack.append(i)

        return res

if __name__ == '__main__':
    t = [73, 74, 75, 71, 69, 72, 76, 73]
    obj = Solution()
    print(obj.dailyTemperatures(t))
