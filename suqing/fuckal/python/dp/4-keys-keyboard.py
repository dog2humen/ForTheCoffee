# coding:utf8
"""
    651. 4键键盘
    假设你有一个特殊的键盘包含下面的按键：
    Key 1: (A)：在屏幕上打印一个 'A'。
    Key 2: (Ctrl-A)：选中整个屏幕。
    Key 3: (Ctrl-C)：复制选中区域到缓冲区。
    Key 4: (Ctrl-V)：将缓冲区内容输出到上次输入的结束位置，并显示在屏幕上。
    现在，你只可以按键 N 次（使用上述四种按键），请问屏幕上最多可以显示几个 'A'呢？
    样例 1:
    输入: N = 3
    输出: 3
    解释: 
    我们最多可以在屏幕上显示三个'A'通过如下顺序按键：
    A, A, A
    链接：https://leetcode-cn.com/problems/4-keys-keyboard
"""
class Solution:
    def maxA(self, N: int) -> int:
        #return self.maxA_v1(N)
        return self.maxA_v2(N)
    def maxA_v1(self, N: int) -> int:
        """
            dp思路
            定义: dp(n, a_num, copy) = x 
            表示操作数n, A的数量, 剪切板中a的数量状态时, 屏幕最多显示a的个数

        """

        memo = {}
        def dp(n: int, a_num: int, copy: int) -> int:

            if n <= 0:
                return a_num
            if (n, a_num, copy) in memo:
                return memo[(n, a_num, copy)]

            res = max(dp(n - 1, a_num + 1, copy), # 按下A
                       dp(n - 1, a_num + copy, copy), # 按下c-v粘贴
                       dp(n - 2, a_num, a_num)) # 按下c-a, c-c
            memo[(n, a_num, copy)] = res
            return memo[(n, a_num, copy)]
            
        return dp(N, 0, 0)
                

    def maxA_v2(self, N: int) -> int:
        """
            最优的操作排列一定是 先按几个A, 然后c-a, c-c, 后连续c-v
            定义: dp[i] = x 表示i次操作后最多能显示多少个A
        """
        dp = [0 for _ in range(N + 1)]
        dp[0] = 0
        for i in range(1, N + 1):
            # 按下A
            dp[i] = dp[i - 1] + 1
            for j in range(2, i):
                # 全选 + 粘贴, 连续粘贴 i - j 次
                dp[i] = max(dp[i], dp[j - 2] * (i - j + 1))
        return dp[N]

if __name__ == '__main__':
    n = 3
    obj = Solution()
    print(obj.maxA(n))
