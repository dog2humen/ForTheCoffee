# coding:utf8
"""
    887. 鸡蛋掉落
    你将获得 K 个鸡蛋，并可以使用一栋从 1 到 N  共有 N 层楼的建筑。
    每个蛋的功能都是一样的，如果一个蛋碎了，你就不能再把它掉下去。
    你知道存在楼层 F ，满足 0 <= F <= N 任何从高于 F 的楼层落下的鸡蛋都会碎，从 F 楼层或比它低的楼层落下的鸡蛋都不会破。
    每次移动，你可以取一个鸡蛋（如果你有完整的鸡蛋）并把它从任一楼层 X 扔下（满足 1 <= X <= N）。
    你的目标是确切地知道 F 的值是多少。
    无论 F 的初始值如何，你确定 F 的值的最小移动次数是多少？

    示例 1：
    输入：K = 1, N = 2
    输出：2
    解释：
    鸡蛋从 1 楼掉落。如果它碎了，我们肯定知道 F = 0 。
    否则，鸡蛋从 2 楼掉落。如果它碎了，我们肯定知道 F = 1 。
    如果它没碎，那么我们肯定知道 F = 2 。
    因此，在最坏的情况下我们需要移动 2 次以确定 F 是多少。
    链接：https://leetcode-cn.com/problems/super-egg-drop
"""
class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        return self.superEggDrop_v1(K, N)
    def superEggDrop_v1(self, K: int, N: int) -> int:
        """
            dp思路
            定义: dp[i][j]表示i个鸡蛋, 楼层为j这个状态下的结果
        """
        
        memo = {}
        def dp(i: int, j: int) -> int:
            

            # 一个鸡蛋, 线性尝试N次
            if i == 1:
                return j
            if j == 0:
                return 0

            if (i, j) in memo:
                return memo[(i, j)]
            
            res = float('INF')
            for k in range(1, j + 1):
                res = min(res,
                    max(dp(i - 1, k - 1), # 碎了
                        dp(i, j - k) # 没碎[i + 1, N]共 N - i层楼
                    ) + 1
                )
            memo[(i, j)] = res
            return memo[(i, j)]
        return dp(K, N)

if __name__ == '__main__':
    k, n = 1, 2
    obj = Solution()
    print(obj.superEggDrop(k, n))
