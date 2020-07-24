# encoding=utf8
"""
1025. 除数博弈
爱丽丝和鲍勃一起玩游戏，他们轮流行动。爱丽丝先手开局。

最初，黑板上有一个数字 N 。在每个玩家的回合，玩家需要执行以下操作：

选出任一 x，满足 0 < x < N 且 N % x == 0 。
用 N - x 替换黑板上的数字 N 。
如果玩家无法执行这些操作，就会输掉游戏。

只有在爱丽丝在游戏中取得胜利时才返回 True，否则返回 false。假设两个玩家都以最佳状态参与游戏。

示例 1：
输入：2
输出：true
解释：爱丽丝选择 1，鲍勃无法进行操作。

示例 2：
输入：3
输出：false
解释：爱丽丝选择 1，鲍勃也选择 1，然后爱丽丝无法进行操作。
"""
class Solution(object):
    # 数学归纳法
    def divisorGame(self, N):
        """
        :type N: int
        :rtype: bool
        """
        return N % 2 == 0
    
    # 根据数学归纳法，找出是否有必胜状态
    # 指定 N=1 和 N=2 的状态
    # 逐步推导出 N 的结果
    def divisorGame_dp(self, N):
        dp = [False] * (N + 2)
        dp[1] = False
        dp[2] = True

        for i in range(3, N + 1):
            for j in range(1, i):
                if i % j == 0 and dp[i-j] == False:
                    dp[i] = True
                    break
        return dp[N]

