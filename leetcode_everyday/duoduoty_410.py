# encoding=utf8
"""
410. 分割数组的最大值
给定一个非负整数数组和一个整数 m，你需要将这个数组分成 m 个非空的连续子数组。
设计一个算法使得这 m 个子数组各自和的最大值最小。

注意:
数组长度 n 满足以下条件:

1 ≤ n ≤ 1000
1 ≤ m ≤ min(50, n)
示例:

输入:
nums = [7,2,5,10,8]
m = 2

输出:
18

解释:
一共有四种方法将nums分割为2个子数组。
其中最好的方式是将其分为[7,2,5] 和 [10,8]，
因为此时这两个子数组各自的和的最大值为18，在所有情况中最小。
"""
class Solution(object):
    """
     dp 定义：
         f[i][j] 表示将数组的前 i 个数分割为 j 段所能得到的最大连续子数组和的最小值

     思考状态转移过程：
         考虑第 j 段的具体范围，即我们可以枚举 k，其中前 k 个数被分割为 j−1 段，而第 k+1 到第 i 个数为第 j 段。
         此时，这 j 段子数组中和的最大值，就等于 f[k][j−1] 与 sub(k+1,i) 中的较大值，
         其中 sub(i,j) 表示数组 nums 中下标落在区间 [i,j] 内的数的和。

     状态转移方程：
         f[i][j] = (k=0) min (i−1) {max(f[k][j−1],sub(k+1,i))}
    """
    def splitArray_dp(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        n = len(nums)
        dp = [[2**32] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        sub = [0]
        for num in nums:
            sub.append(sub[-1] + num)

        for i in range(1, n + 1):
            for j in range(1, min(i, m) + 1):
                for k in range(i):
                    dp[i][j] = min(dp[i][j], max(dp[k][j-1], sub[i] - sub[k]))

        return dp[n][m]

    """
    二分法思路：
        通过二分，逐渐逼近最大和的最小值。
    
    思路详解： 
    check   
        从前到后遍历数组
        total 表示当前分割子数组的和
        cnt 表示已经分割出的子数组的数量（包括当前子数组）
        那么每当 total 加上当前值超过了 x，我们就把当前取的值作为新的一段分割子数组的开头，并将 cnt 加 1。
        遍历结束后验证是否 cnt 不超过 mm。
    
    binary
        二分的
        上界为数组 nums 中所有元素的和，
        下界为数组 nums 中所有元素的最大值。 
    """
    def splitArray_binary_search(self, nums, m):
        def check(x):
            total, cnt = 0, 1
            for num in nums:
                if total + num > x:
                    cnt += 1
                    total = num
                else:
                    total += num
            return cnt <= m

        left = max(nums)
        right = sum(nums)
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left

