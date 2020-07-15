class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n:
            return 0

        dp = [0] * (n + 1)

        dp[0] = 1
        dp[1] = 1
        # 状态：没什么状态，只有 n 这一个，当前有多少个节点  dp(n)
        # 选择：选择有很多，选择 1 ~ n 作为根节点  for i in (1~n)
        ### 难点：状态转移方程中，状态和选择互相有关
        # dp(i)： 总数为 i 的二叉搜索树个数
        # f(j)：以 j 为根，总数为 i 的二叉搜索树个数。 只跟左右子树的个数有关
        # dp(i) = f(1) + f(2) + f(3) + ... + f(i)
        # f(j) = dp(j-1) * dp(i-j) 
        for i in range(2, n+1):
            for j in range(1, i+1):
                dp[i] += dp[j-1] * dp[i-j]

        return dp[n]
