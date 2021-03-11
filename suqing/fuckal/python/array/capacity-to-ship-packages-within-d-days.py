# coding:utf8
"""
    1011. 在 D 天内送达包裹的能力
    传送带上的包裹必须在 D 天内从一个港口运送到另一个港口。
    传送带上的第 i 个包裹的重量为 weights[i]。每一天，我们都会按给出重量的顺序往传送带上装载包裹。我们装载的重量不会超过船的最大运载重量。
    返回能在 D 天内将传送带上的所有包裹送达的船的最低运载能力。

    输入：weights = [1,2,3,4,5,6,7,8,9,10], D = 5
    输出：15
    解释：
    船舶最低载重 15 就能够在 5 天内送达所有包裹，如下所示：
    第 1 天：1, 2, 3, 4, 5
    第 2 天：6, 7
    第 3 天：8
    第 4 天：9
    第 5 天：10

    请注意，货物必须按照给定的顺序装运，因此使用载重能力为 14 的船舶并将包装分成 (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) 是不允许的。 

    链接：https://leetcode-cn.com/problems/capacity-to-ship-packages-within-d-days
"""
from typing import List
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        return self.shipWithinDays_v1(weights, D)

    def shipWithinDays_v1(self, weights: List[int], D: int) -> int:
        
        lo = max(weights)     # 最小载重
        hi = sum(weights) + 1     # 最大载重
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if self.canFinish(weights, D, mid):
                hi = mid 
            else:
                lo = mid + 1
        return lo

    def canFinish(self, weights: List[int], D: int, cap: int) -> bool:
        
        i = 0
        for d in range(D):
            tmp = cap
            tmp -= weights[i]
            while tmp >= 0:
                i += 1
                if i == len(weights):
                    return True
                tmp -= weights[i]
        return False


if __name__ == '__main__':
    weights = [i for i in range(1, 11)]
    print(weights)
    D = 5
    obj = Solution()
    print(obj.shipWithinDays(weights, D))
