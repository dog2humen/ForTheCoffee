# coding:utf8
from typing import List
from collections import Counter
"""
    给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。
    假设每一种面额的硬币有无限个。 

    示例 1:
    输入: amount = 5, coins = [1, 2, 5]
    输出: 4
    解释: 有四种方式可以凑成总金额:
    5=5
    5=2+2+1
    5=2+1+1+1
    5=1+1+1+1+1
    链接：https://leetcode-cn.com/problems/coin-change-2
"""

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        return self.change_v1(amount, coins)

    def change_v1(self, amount: int, coins: List[int]) -> int:
        """
            暴力法, 回溯
	"""
        self.res = 0 
        memo = []
        def helper(target, coins, cur):
            if target == 0:
                if Counter(cur) not in memo:
                    self.res += 1
                    memo.append(Counter(cur))
                return 
            if target < 0:
                return
            for i, coin in enumerate(coins):
                helper(target - coin, coins, cur + [coin])
        
        helper(amount, coins, [])
        return self.res


if __name__ == '__main__':
    amount = 5
    coins = [1, 2, 5]
    obj = Solution()
    print(obj.change(amount, coins))
